# === Stage 22: Add favorite records and quick favorite listing ===
# Project: FitnessJournal
class FavoriteTracker:
    def __init__(self, exercises):
        self.exercises = exercises
        self.favorites = {}

    def add_favorite(self, exercise, record):
        self.favorites[exercise] = record

    def list_favorites(self):
        return list(self.favorites.items())
