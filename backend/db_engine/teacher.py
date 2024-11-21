from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from db_engine.db import Base
from db_engine.classroom import classroom_teacher

        
class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    homeroom = relationship('Classroom', back_populates="homeroom_teacher")
    phone = Column(String)
    
    # Relationship with classrooms
    classrooms = relationship("Classroom", secondary=classroom_teacher, back_populates="teachers")
    
    def to_dict(self, overview=False):
        if overview:
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
                "classrooms": [classroom.name for classroom in self.classrooms],
            }
