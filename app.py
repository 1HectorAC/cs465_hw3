from flask import Flask, jsonify, abort
from datetime import datetime
app = Flask(__name__)

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

@app.route('/api/activities', methods=["GET"])
def activities():
    return jsonify({'activity_log': activity_log})

@app.route('/api/activities/<int:id>', methods=["GET"])
def activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])

@app.route('/')
def hello():
    return "hello"


