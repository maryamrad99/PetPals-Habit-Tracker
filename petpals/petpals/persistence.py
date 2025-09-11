
import json

def save_data(filename: str, data: dict):
    """Save data (habits/pets) to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_data(filename: str) -> dict:
    """Load data (habits/pets) from a JSON file.
    If file does not exist, return an empty dict.
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}