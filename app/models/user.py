import json
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "users.json"

with data_path.open(encoding="utf-8") as f:
    users_data = json.load(f)

users_data = [
    {"id": i, "email": f"user{i}@example.com", "first_name": f"User{i}", "last_name": f"Test"}
    for i in range(1, 21)
]
