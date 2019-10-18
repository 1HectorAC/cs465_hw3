from flask import Flask, jsonify, abort, request
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

@app.route('/api/activities', methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)

    new_entry = request.get_json()
    if 'user_id' not in new_entry or 'username' not in new_entry or 'timestamp' not in new_entry or 'details' not in new_entry:
        abort(400)
    
    new_entry["id"] = 2
    return jsonify(new_entry)


