from flask import Flask
from models import db
from routes import *


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, To-Do API!"

if __name__ == '__main__':
    app.run(debug=True)

