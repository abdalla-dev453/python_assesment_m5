import json
from pathlib import Path

DATABASE_FILE = Path(
    "data/database.json"
)


def load_data():
    if not Path(DATABASE_FILE).exists():
        return {"users": []}
    
    with open(DATABASE_FILE, 'r') as f:
        return json.load(f)
    

def save_data(data):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)