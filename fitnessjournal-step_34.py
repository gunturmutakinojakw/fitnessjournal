# === Stage 34: Add support for multiple local user profiles ===
# Project: FitnessJournal
import json, os, uuid
from pathlib import Path

class ProfileManager:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.profiles_dir = self.data_dir / "profiles"
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.profile_file = self.profiles_dir / "profiles.json"
        self.active_profile = self._load_active()

    def _load_active(self):
        if self.profile_file.exists():
            try:
                return json.loads(self.profile_file.read_text())
            except Exception:
                pass
        return None

    def save_active(self):
        self.profile_file.write_text(json.dumps(self.active_profile))

    def add_profile(self, name, settings=None):
        if settings is None:
            settings = {"weight_kg": 70, "height_cm": 175, "goals": ["strength"]}
        profile = {
            "id": str(uuid.uuid4()),
            "name": name,
            "settings": settings,
            "created": iso8601_now(),
        }
        existing = json.loads(self.profile_file.read_text()) if self.profile_file.exists() else []
        existing.append(profile)
        self.profile_file.write_text(json.dumps(existing, indent=2))
        return profile

    def list_profiles(self):
        existing = json.loads(self.profile_file.read_text()) if self.profile_file.exists() else []
        return existing

    def switch(self, profile_name):
        profiles = self.list_profiles()
        for p in profiles:
            if p["name"].lower() == profile_name.lower():
                self.active_profile = p
                self.save_active()
                return True
        return False

    def delete_profile(self, profile_name):
        profiles = self.list_profiles()
        remaining = [p for p in profiles if p["name"].lower() != profile_name.lower()]
        if len(remaining) == len(profiles):
            return False
        self.profile_file.write_text(json.dumps(remaining, indent=2))
        return True
