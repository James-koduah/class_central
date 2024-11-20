import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from db_engine.control import Control

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def create_app_database():
    engine = create_engine(DATABASE_URL)

    # Check if the database exists, create it if it doesn't
    if not database_exists(engine.url):
        create_database(engine.url)

    Control.initialize(DATABASE_URL)
    Control.create_all()
    tables = ['Student', 'Teacher', 'Course', 'Classroom']
    for table in tables:
        Control.table_migration(table)


if __name__ == "__main__":
    create_app_database()