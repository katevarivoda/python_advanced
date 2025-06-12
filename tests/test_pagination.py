import math

import requests

BASE_URL = "http://localhost:8000"

def test_default_pagination():
    response = requests.get(f"{BASE_URL}/api/users")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 20
    assert data["size"] == 50  # default size
    assert len(data["items"]) == 20


def test_custom_page_size():
    size = 5
    response = requests.get(f"{BASE_URL}/api/users", params={"size": size})
    assert response.status_code == 200
    data = response.json()
    assert data["size"] == size
    total = data["total"]
    expected_pages = math.ceil(total / size)
    assert len(data["items"]) == size
    assert expected_pages == 4


def test_different_pages_return_different_users():
    page1 = requests.get(f"{BASE_URL}/api/users", params={"size": 5, "page": 1}).json()
    page2 = requests.get(f"{BASE_URL}/api/users", params={"size": 5, "page": 2}).json()

    ids_page1 = [user["id"] for user in page1["items"]]
    ids_page2 = [user["id"] for user in page2["items"]]

    assert ids_page1 != ids_page2
    assert len(ids_page1) == 5
    assert len(ids_page2) == 5
