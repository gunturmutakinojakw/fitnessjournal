# === Stage 43: Add CSV import for the primary record type ===
# Project: FitnessJournal
import csv

def import_workouts(csv_path):
    workouts = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            workout = {
                'date': row['date'],
                'routine_name': row['routine_name'],
                'muscle_group': row.get('muscle_group', 'General'),
                'sets': [],
                'notes': row.get('notes', ''),
            }
            for set_row in row['sets'].split(';'):
                parts = set_row.strip().split(',')
                if len(parts) == 4:
                    set_data = {
                        'exercise': parts[0].strip(),
                        'sets_completed': int(parts[1].strip()),
                        'weight': float(parts[2].strip()),
                        'reps': int(parts[3].strip()),
                    }
                    workout['sets'].append(set_data)
            workouts.append(workout)
    return workouts
