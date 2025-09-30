import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from app import app

def test_hello_world():
    """Тест эндпоинта / — должен возвращать приветствие."""
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data


def test_calculate_sum_valid_numbers():
    """Тест суммы с корректными числами."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': [1, 2, 3]}
    )
    assert response.status_code == 200
    assert response.json['total_sum'] == 6.0


def test_calculate_sum_floats():
    """Тест суммы с дробными числами."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': [1.5, 2.5, -1.0]}
    )
    assert response.status_code == 200
    assert response.json['total_sum'] == 3.0


def test_calculate_sum_empty_list():
    """Тест с пустым списком — сумма = 0."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': []}
    )
    assert response.status_code == 200
    assert response.json['total_sum'] == 0.0


def test_calculate_sum_single_number():
    """Тест с одним числом."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': [42]}
    )
    assert response.status_code == 200
    assert response.json['total_sum'] == 42.0


def test_calculate_sum_missing_key():
    """Тест без ключа 'values' — ошибка 400."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'numbers': [1, 2, 3]}
    )
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid request'


def test_calculate_sum_invalid_data_string():
    """Тест с передачей строки вместо числа — ошибка 400."""
    response = app.test_client().post(
        '/calculate_sum',
        json={'values': ["abc", 2, 3]}
    )
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid input data'

def test_calculate_sum_empty_json():
    """Тест с пустым JSON — ошибка 400."""
    response = app.test_client().post('/calculate_sum', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid request'