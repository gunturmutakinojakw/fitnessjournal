# === Stage 19: Add undo support for the last simple mutation ===
# Project: FitnessJournal
import json
from collections import deque

class FitnessJournal:
    def __init__(self):
        self.data = {}
        self.undo_stack = deque(maxlen=100)
    
    def add_routine(self, name, exercises):
        self.data['routines'] = self.data.get('routines', [])
        routine = {'name': name, 'exercises': exercises}
        self.data['routines'].append(routine)
        self.undo_stack.append(('add_routine', {'name': name, 'exercises': exercises}))
        return routine
    
    def add_set(self, routine_name, exercise, sets_info):
        self.data['sets'] = self.data.get('sets', [])
        set_entry = {
            'routine': routine_name,
            'exercise': exercise,
            'sets': sets_info
        }
        self.data['sets'].append(set_entry)
        self.undo_stack.append(('add_set', {'routine': routine_name, 'exercise': exercise, 'sets': sets_info}))
        return set_entry
    
    def set_personal_record(self, routine_name, exercise, weight, reps):
        self.data['records'] = self.data.get('records', [])
        record = {
            'routine': routine_name,
            'exercise': exercise,
            'weight': weight,
            'reps': reps
        }
        self.data['records'].append(record)
        self.undo_stack.append(('set_personal_record', {'routine': routine_name, 'exercise': exercise, 'weight': weight, 'reps': reps}))
        return record
    
    def undo(self):
        if not self.undo_stack:
            return None
        action, info = self.undo_stack.pop()
        self.data['routines'] = self.data.get('routines', [])
        self.data['sets'] = self.data.get('sets', [])
        self.data['records'] = self.data.get('records', [])
        if action == 'add_routine':
            self.data['routines'] = self.data['routines'][:-1]
        elif action == 'add_set':
            self.data['sets'] = self.data['sets'][:-1]
        elif action == 'set_personal_record':
            self.data['records'] = self.data['records'][:-1]
        return info
    
    def save(self, filename='fitness_journal.json'):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def load(self, filename='fitness_journal.json'):
        with open(filename, 'r') as f:
            self.data = json.load(f)
