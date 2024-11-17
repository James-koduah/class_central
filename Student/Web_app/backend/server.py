from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Application running'


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, True)