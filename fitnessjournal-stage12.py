# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: FitnessJournal
import json

def load_workout(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        if 'workouts' not in data:
            raise ValueError("Missing 'workouts' key")
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError as e:
        print(f"Malformed JSON: {e}")
    except ValueError as e:
        print(f"Invalid structure: {e}")
    return None
