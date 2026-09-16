# === Stage 36: Add templates for quickly creating common records ===
# Project: FitnessJournal
def add_record_from_template(self, template_name, **kwargs):
    """Create a record using a predefined template."""
    templates = {
        'push_day': {
            'date': kwargs.get('date', datetime.now().date()),
            'exercises': ['Bench Press', 'Overhead Press', 'Tricep Pushdown'],
            'sets': [3, 3, 3],
            'reps': [10, 10, 15],
            'weight': [80.0, 40.0, 20.0]
        },
        'pull_day': {
            'date': kwargs.get('date', datetime.now().date()),
            'exercises': ['Barbell Row', 'Pull Up', 'Bicep Curl'],
            'sets': [4, 3, 3],
            'reps': [8, 8, 12],
            'weight': [70.0, 0.0, 15.0]
        },
        'legs_day': {
            'date': kwargs.get('date', datetime.now().date()),
            'exercises': ['Squat', 'Lunges', 'Calf Raise'],
            'sets': [5, 3, 4],
            'reps': [8, 12, 15],
            'weight': [100.0, 0.0, 0.0]
        },
        'cardio': {
            'date': kwargs.get('date', datetime.now().date()),
            'exercises': ['Running', 'Cycling'],
            'sets': [1, 1],
            'reps': [30, 45],
            'weight': [0.0, 0.0]
        }
    }
    if template_name not in templates:
        raise ValueError(f"Unknown template: {template_name}. Available: {list(templates.keys())}")
    template = templates[template_name]
    record = WorkoutRecord(
        date=template['date'],
        exercises=template['exercises'],
        sets=template['sets'],
        reps=template['reps'],
        weight=template['weight']
    )
    self._records.append(record)
    return record
