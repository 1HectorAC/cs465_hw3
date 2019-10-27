from datetime import datetime
from random import randint
from flask import Flask, jsonify, abort, request, url_for
from mongoengine import connect, DateTimeField, StringField, IntField, Document
import json

app = Flask(__name__)

app.config.from_envvar('M_APP_SETTINGS')
connect(db=app.config['DATABASE_NAME'], host=app.config['DATABASE_HOST_URL'], port=27017)
class user_activity(Document):
    timestamp = DateTimeField(default=datetime.utcnow)
    username = StringField(required=True, max_length=64)
    user_id = IntField(required=True)
    details = StringField(required=True)

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': "Important stuff here",
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': "Even more important",
    },
]

@app.route('/api/activities/', methods=["GET"])
def activities():
    userList = user_activity.objects.to_json()
    return jsonify({'activity_log': activity_log})

@app.route('/api/activities/<int:id>', methods=["GET"])
def activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])

@app.route('/api/activities', methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)

    new_entry = request.get_json()
    if 'user_id' not in new_entry or 'username' not in new_entry or 'timestamp' not in new_entry or 'details' not in new_entry:
        abort(400)
    
    new_entry["id"] = randint(2,999)
    return jsonify(new_entry)


