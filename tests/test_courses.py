from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../05_2')
from main import app

client = TestClient(app)
_id = None

#'{"msg": "Hello World"}' use '' when not have json in actual_result
def test_hello_msg():
    url = "/hello"
    expected_result = {"msg": "Hello World"}
    actual_result = client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result

def test_post_insert():
    url = "/"
    actual_result = client.post(
        url,
        json= {
            "course_code": "SWE62-353",
            "course_name": "TDD",
            "year": 3,
            "group": 1,
            "number": 30
        }
    )
    expected_result = "SWE62-353"
    global _id
    _id = actual_result.json()['data'][0]['id'] 
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result

def test_get_all():
    url = "/"
    actual_result = client.get(url)
    assert actual_result.status_code == 200

def test_get_by_id():
    url = "/"+_id
    actual_result = client.get(url)
    expected_result = "SWE62-353"
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result

#test_update
def test_put_x_update():
    url = "/"+_id
    actual_result = client.put(
        url,
        json = {
            "course_code": "SWE62-3533",
            "course_name" : "TTD",
            "year" : 3,
            "group" : 1,
            "number" : 30,
        }
    )
    expected_result = "SWE62-3533"
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result

#test_delete
def test_delete_by_id():
    url = "/"+_id
    actual_result = client.delete(url)
    assert actual_result.status_code == 200
    assert actual_result.json()['status'] == 'ok'
