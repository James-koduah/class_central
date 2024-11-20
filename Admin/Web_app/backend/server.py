from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_cors import CORS
from create_database import create_database
from db_engine.student import Student
from db_engine.teacher import Teacher
from db_engine.course import Course
from db_engine.classroom import Classroom
from db_engine.control import Control

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Application running'
        

if __name__ == "__main__":
    create_database()
    app.run('0.0.0.0', 8000, True)