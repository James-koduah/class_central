from flask import Blueprint
student = Blueprint('students', __name__, url_prefix="/students")

from blueprints.students.routes import *