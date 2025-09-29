import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from app import app

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data

def test_calculate_sum():
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': [1, 2, 3]}
    )
    assert response.status_code == 200
    assert response.json['total_sum'] == 6.0