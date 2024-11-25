from flask import Blueprint
course = Blueprint('courses', __name__, url_prefix="/courses")

from blueprints.courses.routes import *