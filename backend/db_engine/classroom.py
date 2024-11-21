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
    
    homeroom_teacher_id = Column(Integer, ForeignKey('teachers.id'))
    homeroom_teacher = relationship("Teacher", back_populates="homeroom", uselist=False)
    teachers = relationship("Teacher", secondary=classroom_teacher, back_populates="classrooms")
    students = relationship("Student", secondary=classroom_student, back_populates="classrooms")
    courses = relationship("Course", secondary=classroom_course, back_populates="classrooms")
    
    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            if k == 'homeroom_teacher':
                self.homeroom_teacher_id = v.id if v else None
            setattr(self, k, v)
    
    def to_dict(self, overview=False):
        if overview:
            return {
                "id": self.id,
                "name": self.name,
                "teachers": len(self.teachers),
                "students": len(self.students),
                "courses": len(self.courses),
                "homeroom_teacher": self.homeroom_teacher.name if self.homeroom_teacher else None,
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "teachers": [teacher.to_dict(overview=True) for teacher in self.teachers],
                "students": [student.to_dict(overview=True) for student in self.students],
                "courses": [course.to_dict(overview=True) for course in self.courses],
                "homeroom_teacher": self.homeroom_teacher.to_dict(overview=True) if self.homeroom_teacher else None,
            }
    