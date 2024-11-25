from sqlalchemy import ForeignKey, String, Column, Integer
from sqlalchemy.orm import relationship
from db_engine.db import Base

# Course class
class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    teacher = relationship("Teacher", back_populates="subjects")
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    classroom = relationship("Classroom", back_populates="courses")
    
    def to_dict(self, overview=False):
        if overview:
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "teacher": self.teacher.name,
                "classroom": self.classroom.name
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "classrooms": [classroom.name for classroom in self.classrooms],
            }