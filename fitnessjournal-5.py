# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: FitnessJournal
def update_record(self, routine_id, exercise_id, data, dry_run=False):
    """Update an existing record or create a new one.
    Args:
        routine_id: The ID of the routine.
        exercise_id: The ID of the exercise.
        data: A dictionary with keys like 'date', 'weight', 'reps', 'sets', 'notes'.
        dry_run: If True, simulate the update without modifying the file.
    Returns:
        A dictionary with 'success', 'message', and 'record' keys.
    """
    if dry_run:
        return {'success': True, 'message': 'Dry run complete, no changes made.', 'record': None}

    try:
        with open(self.file_path, 'r') as f:
            records = json.load(f)
    except FileNotFoundError:
        return {'success': False, 'message': 'File not found, please create the database first.', 'record': None}

    key = f"{routine_id}:{exercise_id}"
    if key in records:
        records[key].update(data)
        with open(self.file_path, 'w') as f:
            json.dump(records, f, indent=4)
        return {'success': True, 'message': 'Record updated successfully.', 'record': records[key]}
    else:
        new_record = {'routine_id': routine_id, 'exercise_id': exercise_id, **data}
        records[key] = new_record
        with open(self.file_path, 'w') as f:
            json.dump(records, f, indent=4)
        return {'success': True, 'message': 'Record created successfully.', 'record': new_record}
