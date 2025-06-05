import requests


def test_user_data():
    response = requests.get("http://localhost:8000/api/users/1")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1


def test_user_not_found():
    response = requests.get("http://localhost:8000/api/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_user_data_email():
    response = requests.get("http://localhost:8000/api/users/1")
    assert response.status_code == 200
    user = response.json()["data"]
    assert "email" in user
    assert user["email"].endswith("@reqres.in")


def test_user_data_keys():
    response = requests.get("http://localhost:8000/api/users/1")
    assert response.status_code == 200
    user = response.json()["data"]
    assert set(user.keys()) == {"id", "email", "first_name", "last_name"}
