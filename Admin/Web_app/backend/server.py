from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Application running'


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, True)