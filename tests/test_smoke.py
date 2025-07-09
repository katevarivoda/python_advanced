import requests

BASE_URL = "http://localhost:8000"


def test_status_alive():
    response = requests.get(f"{BASE_URL}/api/status")
    assert response.status_code == 200
    assert response.json() == {"database": True}


def test_docs_available():
    response = requests.get(f"{BASE_URL}/docs")
    assert response.status_code == 200
    assert "Swagger UI" in response.text


def test_openapi_schema():
    response = requests.get(f"{BASE_URL}/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == "Reqres Clone"


def test_existing_user(fill_test_data):
    user_id = fill_test_data[0]
    response = requests.get(f"http://localhost:8000/api/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id



def test_non_existing_user_returns_404():
    response = requests.get(f"{BASE_URL}/api/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_unknown_path_returns_404():
    response = requests.get(f"{BASE_URL}/not/a/real/path")
    assert response.status_code == 404
