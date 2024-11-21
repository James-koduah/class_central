from blueprints.classrooms import classroom
from flask import request
from db_engine.classroom import Classroom
from db_engine.teacher import Teacher
from db_engine.control import Control
from utils import resp

@classroom.route('/', methods=['get', 'post'], strict_slashes=False)
def classrooms():
    """Get all instances of classroom from the database
    GET METHOD: Simply returns all instances of Classrooms
    POST METHOD: Specify filters to filter instances.
    """
    if request.method == 'GET':
        with Control.start_session() as session:
            classrooms = session.query(Classroom).all()
            response = [classroom.to_dict(overview=True) for classroom in classrooms]
            return resp(True, data=response)
        

@classroom.route('/new_classroom', methods=['post'], strict_slashes=False)
def new_classroom():
    """Make a new classroom entry into the database"""
    data = request.get_json()
    name = data.get('name')
    homeroom_teacher_id = data.get('homeroom_teacher_id', None)
    homeroom_teacher = None
    if not name or name == '':
        return resp(False, message="Classroom must have a name")
    
    with Control.start_session() as session:
        # Check if a classroom with the same name already exists
        check = session.query(Classroom).filter(Classroom.name==name).first()
        if check:
            return resp(False, message="A Classroom with this name already exists")
        
        # If the teacher id is specified, check if Teacher exists and assign to classroom. Else Teacher is None.
        if homeroom_teacher_id:
            homeroom_teacher = session.query(Teacher).filter(Teacher.id==homeroom_teacher_id).first()
            if not homeroom_teacher:
                return resp(False, message="No such Teacher Exists in the database")
        
        classroom_obj = Classroom()
        classroom_obj.update(
            name=name,
            homeroom_teacher=homeroom_teacher
        )
        session.add(classroom_obj)
        session.commit()
    return resp(True, message="Classroom Successfully Created")

@classroom.route('/update_classroom', methods=['post'], strict_slashes=False)
def update_classroom():
    data = request.get_json()
    classroom_id = data.get('classroom_id')
    name = data.get('name')
    homeroom_teacher_id = data.get('homeroom_teacher_id', None)
    homeroom_teacher = None
    if not name or name == '' or not classroom_id:
        return resp(False, message="Bad data. Missing classroom_id or name")
    
    with Control.start_session() as session:
        # Check if the classroom exists
        classroom = session.query(Classroom).filter(Classroom.id==classroom_id).first()
        if not classroom:
            return resp(False, message="No such classroom found in database")
        
        # Check if the new name we want to give the classroom already exists
        check = session.query(Classroom).filter(Classroom.name==name).first()
        if check:
            return resp(False, message="A Classroom with this name already exists")
        
        # If the teacher id is specified, check if Teacher exists and assign to classroom. Else Teacher is None.
        if homeroom_teacher_id:
            homeroom_teacher = session.query(Teacher).filter(Teacher.id==homeroom_teacher_id).first()
            if not homeroom_teacher:
                return resp(False, message="No such Teacher Exists in the database")
        
        classroom.update(
            name=name,
            homeroom_teacher=homeroom_teacher
        )
        session.commit()
    return resp(True, message="Classroom Updated Sucessfully")
    