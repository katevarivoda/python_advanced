import requests

BASE_URL = "http://localhost:8000"


def test_status_alive():
    """Проверка /status"""
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_docs_available():
    """Swagger доступен"""
    response = requests.get(f"{BASE_URL}/docs")
    assert response.status_code == 200
    assert "Swagger UI" in response.text


def test_openapi_schema():
    """OpenAPI схема доступна"""
    response = requests.get(f"{BASE_URL}/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == "Reqres Clone"


def test_existing_user():
    """Проверка существующего пользователя"""
    response = requests.get(f"{BASE_URL}/api/users/1")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1


def test_non_existing_user_returns_404():
    """Пользователь не найден"""
    response = requests.get(f"{BASE_URL}/api/users/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_unknown_path_returns_404():
    """Случайный путь должен вернуть 404"""
    response = requests.get(f"{BASE_URL}/not/a/real/path")
    assert response.status_code == 404
