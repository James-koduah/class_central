from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from db_engine.db import Base
from db_engine.classroom import classroom_course

# Course class
class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    # Relationship with classrooms
    classrooms = relationship("Classroom", secondary=classroom_course, back_populates="courses")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "classrooms": [classroom.class_name for classroom in self.classrooms],
        }