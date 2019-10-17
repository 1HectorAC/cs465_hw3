from flask import Flask, jsonify
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

@app.route('/')
def hello():
    return "hello"


