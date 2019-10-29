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

@app.route('/api/activities/', methods=["GET"])
def activities():
    return_log = user_activity.objects.to_json()
    logList = json.loads(return_log)
    logList = logList[-app.config['N']:]
    #fix formating of timestamp and id for each entry
    if(len(logList) > 0):
        for i in range(len(logList)):
            logList[i]["timestamp"] = str(datetime.utcfromtimestamp(int(logList[i]["timestamp"]["$date"] / 1000)))
            logList[i]["id"] = str(logList[i]["_id"]["$oid"])
            logList[i].pop("_id")
    
    return jsonify({'activity_log': logList})

@app.route('/api/activities/<string:id>', methods=["GET"])
def activity(id):
    return_activity = user_activity.objects(id = id).to_json()
    activityDict = json.loads(return_activity)

    #fix formating of timestamp and id
    activityDict[0]["timestamp"] = str(datetime.utcfromtimestamp(int(activityDict[0]["timestamp"]["$date"] / 1000)))
    activityDict[0]["id"] = str(activityDict[0]["_id"]["$oid"])
    activityDict[0].pop("_id")

    return jsonify(activityDict[0])

@app.route('/api/activities', methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)
    new_entry = request.get_json()
    if 'user_id' not in new_entry or 'username' not in new_entry or 'details' not in new_entry:
        abort(400)
    
    enteredTimeStamp = ""
    if "timestamp" not in new_entry:
        enteredTimeStamp = datetime.utcnow()
    else:
        enteredTimeStamp = new_entry["timestamp"]

    new_activity = user_activity(
        timestamp = enteredTimeStamp,
        username = new_entry["username"],
        user_id = new_entry["user_id"],
        details = new_entry["details"]
    )
    new_activity.save()

    activityDict = user_activity.objects(id = new_activity["id"]).to_json()
    newActivityDict = json.loads(activityDict)

    #fix format of id and timestamp
    newActivityDict[0]["id"] = str(newActivityDict[0]["_id"]["$oid"])
    newActivityDict[0].pop("_id")
    newActivityDict[0]["timestamp"] = str(datetime.utcfromtimestamp(int(newActivityDict[0]["timestamp"]["$date"] / 1000)))

    newActivityDict[0]["location"] = url_for("activities", id = newActivityDict[0]["id"])

    return jsonify(newActivityDict[0]), 201


