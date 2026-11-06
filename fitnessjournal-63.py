# === Stage 63: Add relationships between records where useful ===
# Project: FitnessJournal
class Record:
    def __init__(self, exercise_id=None, routine_id=None, weight=None, reps=None,
                 date=None, note=None):
        self.exercise_id = exercise_id
        self.routine_id = routine_id
        self.weight = weight
        self.reps = reps
        self.date = date
        self.note = note
        self.linked_records = []

    def link(self, other):
        if other is not self:
            if other not in self.linked_records:
                self.linked_records.append(other)
            if self not in other.linked_records:
                other.linked_records.append(self)

    def unlink(self, other):
        if other in self.linked_records:
            self.linked_records.remove(other)
        if self in other.linked_records:
            other.linked_records.remove(self)

    def most_recent(self):
        latest = self
        for linked in self.linked_records:
            if linked.date and (latest.date is None or linked.date > latest.date):
                latest = linked
        return latest

    def chain(self):
        seen = set()
        order = []
        stack = [self]
        while stack:
            record = stack.pop()
            if id(record) in seen:
                continue
            seen.add(id(record))
            order.append(record)
            stack.extend(record.linked_records)
        return order

    def total_exercises(self):
        return len(self.chain())
