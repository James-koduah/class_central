from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from create_database import create_app_database

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_KEY')
jwt = JWTManager(app)
CORS(app)

from blueprints.classrooms import classroom
app.register_blueprint(classroom)


"""
Standard JSON Response Format
{
    'status': True|Success or False|Failure,
    'data': Information|Usually returned on success
    'message': Text Description|Usually returned on Failure
}
"""
        

if __name__ == "__main__":
    create_app_database()
    app.run('0.0.0.0', 8000, True)