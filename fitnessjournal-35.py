# === Stage 35: Add active user switching and user-specific records ===
# Project: FitnessJournal
import json
import os
from datetime import datetime

DATA_FILE = "fitness_journal.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "current_user": None}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def register_user(name):
    data = load_data()
    if data["current_user"] is None:
        data["current_user"] = name
    if name not in data["users"]:
        data["users"][name] = {"records": {}, "workouts": [], "created_at": datetime.now().isoformat()}
    save_data(data)
    return data["users"][name]

def add_record(user_name, exercise, weight, reps, date=None):
    data = load_data()
    if data["current_user"] != user_name:
        print(f"Error: Current user is '{data['current_user']}', not '{user_name}'")
        return
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    key = f"{exercise}_{reps}_{weight}"
    record = {"weight": weight, "reps": reps, "date": date}
    if key in data["users"][user_name]["records"]:
        print("Record already exists!")
        return
    data["users"][user_name]["records"][key] = record
    save_data(data)
    return record

def show_records(user_name):
    data = load_data()
    if data["current_user"] != user_name:
        print(f"Error: Current user is '{data['current_user']}', not '{user_name}'")
        return
    records = data["users"][user_name]["records"]
    if not records:
        print("No records yet.")
        return
    print(f"\nRecords for {user_name}:")
    for key, rec in records.items():
        print(f"  {key}: {rec['weight']} kg x {rec['reps']} reps on {rec['date']}")
