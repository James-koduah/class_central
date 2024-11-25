from sqlalchemy import or_
from db_engine.teacher import Teacher
from db_engine.classroom import Classroom
from blueprints.courses import course
from flask import request
from db_engine.course import Course 
from db_engine.student import Student
from db_engine.control import Control
from utils import resp

@course.route('/', methods=['get', 'post'], strict_slashes=False)
def courses():
    """Get all instances of courses from the database
    GET METHOD: Simply returns all instances of courses
    POST METHOD: Specify filters to filter instances.
    """
    if request.method == 'GET':
        with Control.start_session() as session:
            courses = session.query(Course).join(Course.classroom).order_by(Classroom.name).all()
            response = [course.to_dict(overview=True) for course in courses]
            return resp(True, data=response)
        

@course.route('/new_course', methods=['post'], strict_slashes=False)
def new_course():
    """Make a new Course entry into the database"""
    data = request.get_json()
    name = data.get('name', '')
    description = data.get("description")
    classroom_id = data.get('classroom_id')
    teacher_id = data.get('teacher_id')
    if name == '' or not classroom_id or not teacher_id:
        return resp(False, message="Bad request. Missing Fields [name, classroom_id, teacher_id]")
    
    with Control.start_session() as session:
        classroom = session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            return resp(False, message="Error, Classroom cannot be found.")
        
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            return resp(False, message="Error, Teacher cannot be found.")
        
        check = session.query(Course).filter(or_(Course.name == name, Course.classroom_id == classroom_id)).first()
        if check:
            return resp(False, message="A Course in this classroom with the same name already exists")
        
        course_obj = Course(
            name=name,
            description=description,
            classroom=classroom,
            teacher=teacher
        )
        session.add(course_obj)
        session.commit()
    return resp(True, message="Student Successfully Created")

@course.route('/update_course', methods=['post'], strict_slashes=False)
def update_teacher():
    data = request.get_json()
    name = data.get('name', '')
    course_id = data.get('course_id')
    description = data.get("description")
    classroom_id = data.get('classroom_id')
    teacher_id = data.get('teacher_id')
    if name == '' or not course_id:
        return resp(False, message="Bad request. Missing Fields [name, classroom_id, teacher_id, course_id]")
    
    with Control.start_session() as session:
        # Check if the Course exists
        course = session.query(Course).filter(Course.id==course_id).first()
        if not course:
            return resp(False, message="No such course found in database")
        
        if classroom_id:
            classroom = session.query(Classroom).filter(Classroom.id == classroom_id).first()
            course.classroom = classroom
                    
        if teacher_id:
            teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
            course.teacher = teacher
        
        course.name = name        
        course.description = description
        session.commit()
        
    return resp(True, message="Course Updated Sucessfully")
    