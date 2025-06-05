import json
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data" / "users.json"

with data_path.open(encoding="utf-8") as f:
    users_data = json.load(f)
