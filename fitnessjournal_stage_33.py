# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: FitnessJournal
SETTINGS = {
    "default_units": "metric",
    "weight_unit": "kg",
    "distance_unit": "km",
    "time_unit": "seconds",
    "display_format": "compact",
    "notifications_enabled": True,
    "theme": "dark",
    "last_updated": None,
}


def get_setting(key):
    if key not in SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    return SETTINGS[key]


def set_setting(key, value):
    if key not in SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    SETTINGS[key] = value
    SETTINGS["last_updated"] = datetime.now().isoformat()
    print(f"Setting '{key}' updated to {value!r}")
    return SETTINGS[key]


def reset_settings():
    SETTINGS["last_updated"] = datetime.now().isoformat()
    print("All settings reset to defaults")
    return SETTINGS
