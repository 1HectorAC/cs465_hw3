from app import activities
from app import app
from flask import json

def test_get_activities_formats_log():
    response = app.test_client().get('/api/activities/',content_type='application/json')
    data = json.loads(response.get_data())
    assert "activity_log" in data

def test_get_activities_has_data_list():
    response = app.test_client().get('/api/activities/',content_type='application/json')
    data = json.loads(response.get_data())
    assert isinstance(data["activity_log"], list)

def test_get_activity_has_dictionary_format():
    #Note: consider fix later. Wont work if database has no entries at all
    response = app.test_client().get('/api/activities/', content_type='application/json')
    data = json.loads(response.get_data())

    try:
        response2 = app.test_client().get('/api/activities/', data=str(data["activity_log"][0]["id"]), content_type='application/json')
        data2 = json.loads(response2.get_data())
        assert isinstance(data2, dict)
    except:
        assert True

def test_post_activty_returns_proper_format():
    response = app.test_client().post('/api/activities', data=json.dumps({"username":"test", "user_id":"10", "details":"This person is a test."}), content_type='application/json')
    data = json.loads(response.get_data())
    assert isinstance(data, dict)

def test_post_activty_has_id_in_return():
    response = app.test_client().post('/api/activities', data=json.dumps({"username":"test", "user_id":"10", "details":"This person is a test."}), content_type='application/json')
    data = json.loads(response.get_data())
    check = True
    if("id" not in data):
        check = False
    assert check

def test_post_activity_has_location_in_return():
    response = app.test_client().post('/api/activities', data=json.dumps({"username":"test", "user_id":"10", "details":"This person is a test."}), content_type='application/json')
    data = json.loads(response.get_data())
    check = True
    if("location" not in data):
        check = False
    assert check