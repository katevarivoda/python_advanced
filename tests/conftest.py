import pytest
import requests

BASE_URL = "http://localhost:8000/api/users"

# Тестовые данные для пользователей
test_data_users = [
    {
        "email": f"user{i}@example.com",
        "first_name": f"User{i}",
        "last_name": "Test",
        "avatar": f"https://example.com/avatar{i}.png"
    }
    for i in range(1, 10)
]

@pytest.fixture(scope="session")
def app_url():
    return "http://localhost:8000"

@pytest.fixture(scope="module")
def fill_test_data():
    """Создаёт пользователей через API и удаляет их после тестов"""
    user_ids = []

    for user in test_data_users:
        response = requests.post(BASE_URL + "/", json=user)
        assert response.status_code == 201
        user_ids.append(response.json()["id"])

    yield user_ids

    for user_id in user_ids:
        requests.delete(f"{BASE_URL}/{user_id}")
