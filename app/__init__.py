import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Ximena Vazquez Mellado", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="My Hobbies", url=os.getenv("URL"))

@app.route('/experience')
def projects():
    return render_template('experience.html', title="My Experience", url=os.getenv("URL"))