# === Stage 13: Add file save support using a configurable path ===
# Project: FitnessJournal
import os

class SaveConfig:
    """Handles saving workout data to a configurable file path."""

    def __init__(self, file_path="fitness_journal.json"):
        self.file_path = file_path

    def save(self, data):
        """Saves the workout data to the configured file path."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {self.file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load(self):
        """Loads the workout data from the configured file path."""
        if not os.path.exists(self.file_path):
            print("No data file found.")
            return {}
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            print(f"Data loaded from {self.file_path}")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}
