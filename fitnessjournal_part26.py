# === Stage 26: Add weekly summary calculations ===
# Project: FitnessJournal
class WeeklySummary:
    def __init__(self, week_start, week_end):
        self.week_start = week_start
        self.week_end = week_end
        self.exercises = []

    def add(self, exercise):
        self.exercises.append(exercise)

    def total_sets(self):
        return sum(e.sets for e in self.exercises)

    def total_volume(self):
        return sum(e.volume for e in self.exercises)

    def total_weight(self):
        return sum(e.weight for e in self.exercises)

    def avg_sets(self):
        return sum(e.sets for e in self.exercises) / len(self.exercises) if self.exercises else 0

    def __str__(self):
        lines = [f"Weekly Summary ({self.week_start} - {self.week_end}):\n"]
        lines.append(f"  Total Sets: {self.total_sets()}\n")
        lines.append(f"  Total Volume (kg): {self.total_volume()}\n")
        lines.append(f"  Total Weight (kg): {self.total_weight()}\n")
        lines.append(f"  Average Sets per Exercise: {self.avg_sets():.1f}")
        return "".join(lines)
