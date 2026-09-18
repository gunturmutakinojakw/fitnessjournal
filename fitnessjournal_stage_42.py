# === Stage 42: Add CSV export without external dependencies ===
# Project: FitnessJournal
import csv
import os
from datetime import datetime

def export_to_csv(workouts, filename="fitness_journal_export.csv"):
    """Export workout data to a CSV file."""
    if not workouts:
        return
    fieldnames = ["Date", "Routine", "Exercise", "Sets", "Reps", "Weight", "Notes"]
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for w in workouts:
            writer.writerow({
                "Date": datetime.fromisoformat(w["date"]).strftime("%Y-%m-%d"),
                "Routine": w["routine"],
                "Exercise": w["exercise"],
                "Sets": w["sets"],
                "Reps": w["reps"],
                "Weight": w.get("weight", 0),
                "Notes": w.get("notes", ""),
            })
    print(f"Exported {len(workouts)} workouts to {filepath}")
