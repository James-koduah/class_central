from flask import Blueprint
classroom = Blueprint('classroom', __name__, url_prefix="/classrooms")

from blueprints.classrooms.routes import *