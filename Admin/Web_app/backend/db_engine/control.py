from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from db_engine.db import Base
from db_engine.student import Student
from db_engine.teacher import Teacher
from db_engine.course import Course
from db_engine.classroom import Classroom


class Control:
    """A class that provides an interface for easy usage of data from database"""

    engine = None
    session_factory = None

    @classmethod
    def initialize(cls, database_url: str):
        """Initialize the control class"""
        cls.engine = create_engine(database_url)
        cls.session_factory = sessionmaker(bind=cls.engine)

    @classmethod
    def create_all(cls):
        """Create all tables"""
        Base.metadata.create_all(bind=cls.engine)

    @classmethod
    def start_session(cls):
        """Starts a session"""
        return cls.session_factory()
    
    @classmethod
    def table_migration(cls, table_class):
        """Create or update a table and columns"""
        table = eval(table_class)
        table_name = table.__tablename__
        inspector = inspect(cls.engine)

        # If table does not exist, create it
        if not inspector.has_table(table.__tablename__):
            cls.create_all()
            print(f"Table '{table.__tablename__}' created successfully.")

        # If table exists, check if columns exist and create and update them if they don't
        with cls.engine.connect() as connection:
            columns = [col for col in table.__table__.columns]
            for col in columns:
                column_name = col.name
                column_type = col.type
                query = text(
                    f"""
                    DO $$
                    BEGIN
                        IF NOT EXISTS (
                            SELECT 1
                            FROM information_schema.columns
                            WHERE table_name = '{table_name}' AND column_name = '{column_name}'
                        ) THEN
                            EXECUTE 'ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}';
                        ELSE
                            EXECUTE 'ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {column_type} USING {column_name}::{column_type}';
                        END IF;
                    END $$;
                    """
                )
                connection.execute(query)
                connection.commit()
                

        # Check if a column in the database is no longer defined in the Class and delete it
        with cls.engine.connect() as connection:
            # Get existing columns from the database table
            existing_columns = {
                col["name"] for col in inspector.get_columns(table_name)
            }
            # Get columns defined in the ORM class
            orm_columns = {column.name for column in table.__table__.columns}
            # Find columns to drop
            columns_to_drop = existing_columns - orm_columns
            for column in columns_to_drop:
                query = text(f"ALTER TABLE {table_name} DROP COLUMN {column}")
                connection.execute(query)
                connection.commit()
                print(
                    f"Column '{column}' dropped successfully from '{table_name}'."
                )
