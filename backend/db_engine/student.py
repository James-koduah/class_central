from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from db_engine.db import Base
from db_engine.classroom import classroom_student


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    grade_level = Column(String)
    
    # Relationship with classrooms
    classrooms = relationship("Classroom", secondary=classroom_student, back_populates="students")
    
    def to_dict(self, overview=False):
        if overview:
            return {
                "id": self.id,
                "name": self.name,
                "grade_level": self.grade_level
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "grade_level": self.grade_level,
                "classrooms": [classroom.name for classroom in self.classrooms],
            }