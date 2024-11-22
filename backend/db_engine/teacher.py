from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from db_engine.db import Base
from db_engine.classroom import classroom_teacher

        
class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    honorific = Column(String)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    position = Column(String)
    homeroom = relationship('Classroom', back_populates="homeroom_teacher")
    
    # Relationship with classrooms
    classrooms = relationship("Classroom", secondary=classroom_teacher, back_populates="teachers")
    
    def to_dict(self, overview=False):
        if overview:
            return {
                "id": self.id,
                "honorific": self.honorific,
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
                "position": self.position
            }
        else:
            return {
                "id": self.id,
                "honorific": self.honorific,
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
                "position": self.position,
                "classrooms": [classroom.name for classroom in self.classrooms],
            }
