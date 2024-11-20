from sqlalchemy import ForeignKey, String, Column, Integer, Table
from sqlalchemy.orm import relationship
from db_engine.db import Base
 

# Association tables
classroom_teacher = Table(
    "classroom_teacher",
    Base.metadata,
    Column("classroom_id", Integer, ForeignKey("classrooms.id"), primary_key=True),
    Column("teacher_id", Integer, ForeignKey("teachers.id"), primary_key=True)
)

classroom_student = Table(
    "classroom_student",
    Base.metadata,
    Column("classroom_id", Integer, ForeignKey("classrooms.id"), primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True)
)

classroom_course = Table(
    "classroom_course",
    Base.metadata,
    Column("classroom_id", Integer, ForeignKey("classrooms.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)   


class Classroom(Base):
    __tablename__ = "classrooms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teachers = relationship("Teacher", secondary=classroom_teacher, back_populates="classrooms")
    students = relationship("Student", secondary=classroom_student, back_populates="classrooms")
    courses = relationship("Course", secondary=classroom_course, back_populates="classrooms")
    
    def to_dict(self):
        return {
            "id": self.id,
            "class_name": self.class_name,
        }
    