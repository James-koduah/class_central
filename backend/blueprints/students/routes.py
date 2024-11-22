from sqlalchemy import or_
from blueprints.students import student
from flask import request
from db_engine.classroom import Classroom
from db_engine.student import Student
from db_engine.control import Control
from utils import resp

@student.route('/', methods=['get', 'post'], strict_slashes=False)
def students():
    """Get all instances of students from the database
    GET METHOD: Simply returns all instances of students
    POST METHOD: Specify filters to filter instances.
    """
    if request.method == 'GET':
        with Control.start_session() as session:
            students = session.query(Student).order_by(Student.name).all()
            response = [student.to_dict(overview=True) for student in students]
            return resp(True, data=response)
        

@student.route('/new_student', methods=['post'], strict_slashes=False)
def new_student():
    """Make a new Student entry into the database"""
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    gender = data.get('gender', '')
    guardian = data.get('guardian', '')
    if name == '' or email == '' or phone == '':
        return resp(False, message="Bad request. Missing Fields [name, email, phone]")
    
    with Control.start_session() as session:
        check = session.query(Student).filter(Student.email == email).first()
        if check:
            return resp(False, message="A Student with this email already exists")
        
        student_obj = Student(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            guardian=guardian        
        )
        session.add(student_obj)
        session.commit()
    return resp(True, message="Student Successfully Created")

@student.route('/update_student', methods=['post'], strict_slashes=False)
def update_teacher():
    data = request.get_json()
    student_id = data.get('student_id')
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    gender = data.get('gender', '')
    guardian = data.get('guardian', '')
    if name == '' or email == '' or not student_id:
        return resp(False, message="Bad data. Missing student_id or name or email")
    
    with Control.start_session() as session:
        # Check if the Student exists
        student = session.query(Student).filter(Student.id==student_id).first()
        if not student:
            return resp(False, message="No such student found in database")
        
        student.name = name
        student.email = email
        student.phone = phone
        student.gender = gender
        student.guardian = guardian
        session.commit()
        
    return resp(True, message="Student Updated Sucessfully")
    