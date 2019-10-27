from app import activities
from app import app
from flask import json

def test_get_activities_formats_log():
    response = app.test_client().get('/api/activities/',content_type='application/json')
    data = json.loads(response.get_data())
    assert "activity_log" in data
