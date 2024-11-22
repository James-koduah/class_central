from sqlalchemy import or_
from blueprints.teachers import teacher
from flask import request
from db_engine.classroom import Classroom
from db_engine.teacher import Teacher
from db_engine.control import Control
from utils import resp

@teacher.route('/', methods=['get', 'post'], strict_slashes=False)
def teacherss():
    """Get all instances of teachers from the database
    GET METHOD: Simply returns all instances of teachers
    POST METHOD: Specify filters to filter instances.
    """
    if request.method == 'GET':
        with Control.start_session() as session:
            teachers = session.query(Teacher).order_by(Teacher.name).all()
            response = [teacher.to_dict(overview=True) for teacher in teachers]
            return resp(True, data=response)
        

@teacher.route('/new_teacher', methods=['post'], strict_slashes=False)
def new_teacher():
    """Make a new teacher entry into the database"""
    data = request.get_json()
    honorific = data.get('honorific', '')
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    if name == '' or email == '' or phone == '' or honorific == '':
        return resp(False, message="Bad request. Missing Fields [honorific, name, email, phone]")
    
    with Control.start_session() as session:
        check = session.query(Teacher).filter(
            or_(Teacher.name == name, Teacher.email == email)
        ).first()
        if check:
            return resp(False, message="A Teacher with this name or email alread exists")
        
        teacher_obj = Teacher(
            honorific=honorific,
            name=name,
            email=email,
            phone=phone            
        )
        session.add(teacher_obj)
        session.commit()
    return resp(True, message="Classroom Successfully Created")

@teacher.route('/update_teacher', methods=['post'], strict_slashes=False)
def update_teacher():
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    honorific = data.get('honorific', '')
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    if name == '' or email == '' or not teacher_id:
        return resp(False, message="Bad data. Missing teacher_id or name or email")
    
    with Control.start_session() as session:
        # Check if the teacher exists
        teacher = session.query(Teacher).filter(Teacher.id==teacher_id).first()
        if not teacher:
            return resp(False, message="No such teacher found in database")
        
        
        teacher.honorific = honorific,
        teacher.name = name,
        teacher.email = email,
        teacher.phone = phone
        session.commit()
        
    return resp(True, message="Teacher Updated Sucessfully")
    