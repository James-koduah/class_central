from flask import Blueprint
teacher = Blueprint('teachers', __name__, url_prefix="/teachers")

from blueprints.teachers.routes import *