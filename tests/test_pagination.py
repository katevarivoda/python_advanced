import math
import pytest
import requests

BASE_URL = "http://localhost:8000/api/users"


@pytest.fixture(scope="module")
def total_users():
    response = requests.get(BASE_URL, params={"page": 1, "size": 100})
    assert response.status_code == 200
    return response.json()["total"]


def test_default_pagination(total_users):
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()

    assert data["page"] == 1
    assert data["size"] == 50  # значение по умолчанию
    assert data["total"] == total_users

    expected_pages = math.ceil(total_users / data["size"])
    assert data["pages"] == expected_pages
    assert len(data["items"]) <= data["size"]


@pytest.mark.parametrize("size", [1, 5, 10, 15])
def test_custom_page_size(size, total_users):
    response = requests.get(BASE_URL, params={"page": 1, "size": size})
    assert response.status_code == 200
    data = response.json()

    assert data["size"] == size
    assert data["page"] == 1
    assert data["total"] == total_users

    expected_pages = math.ceil(total_users / size)
    assert data["pages"] == expected_pages
    assert len(data["items"]) <= size


def test_different_pages_return_different_users():
    size = 5
    page1 = requests.get(BASE_URL, params={"size": size, "page": 1}).json()
    page2 = requests.get(BASE_URL, params={"size": size, "page": 2}).json()

    ids_page1 = {user["id"] for user in page1["items"]}
    ids_page2 = {user["id"] for user in page2["items"]}

    assert ids_page1.isdisjoint(ids_page2)
    assert len(ids_page1) <= size
    assert len(ids_page2) <= size

