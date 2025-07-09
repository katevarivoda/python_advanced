import pytest
import requests
from http import HTTPStatus
from app.models.User import User

BASE_URL = "http://localhost:8000/api/users"


@pytest.mark.usefixtures("fill_test_data")
def test_users_list_available():
    """Проверка, что список пользователей отдается"""
    response = requests.get(BASE_URL)
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert isinstance(data["items"], list)
    assert len(data["items"]) >= 5
    for user in data["items"]:
        User.model_validate(user)


@pytest.mark.usefixtures("fill_test_data")
def test_users_no_duplicates():
    """Проверка на уникальность ID пользователей"""
    response = requests.get(BASE_URL)
    ids = [user["id"] for user in response.json()["items"]]
    assert len(ids) == len(set(ids))


def test_get_single_user(fill_test_data):
    """Получение первого и последнего пользователя из фикстуры"""
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        r = requests.get(f"{BASE_URL}/{user_id}")
        assert r.status_code == HTTPStatus.OK
        user = r.json()
        User.model_validate(user)
        assert user["id"] == user_id


@pytest.mark.parametrize("user_id", [999999])
def test_get_nonexistent_user_returns_404(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "User not found"


@pytest.mark.parametrize("user_id", [-1, 0, "invalid"])
def test_get_invalid_user_id_returns_422(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
