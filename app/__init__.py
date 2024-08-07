import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("App running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    # Connection to the database through environment variables .env
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
                        user=os.getenv("MYSQL_USER"), 
                        password=os.getenv("MYSQL_PASSWORD"), 
                        host=os.getenv("MYSQL_HOST"), 
                        port=3306
                        )

#print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta():
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="Ximena Vazquez Mellado", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="My Hobbies", url=os.getenv("URL"))

@app.route('/experience')
def projects():
    return render_template('experience.html', title="My Experience", url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title='Timeline Posts', url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    # Validate form data and sending error messages
    if not name:
        return "Invalid name", 400
    if not email or '@' not in email:
        return "Invalid email", 400
    if not content:
        return "Invalid content", 400
    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_last_time_line_post():
    try:
        last_post = TimelinePost.select().order_by(TimelinePost.created_at.desc()).get()
        last_post.delete_instance()
        return jsonify({"message": "Last timeline post deleted successfully."}), 200
    except TimelinePost.DoesNotExist:
        return jsonify({"error": "No timeline posts found."}), 404