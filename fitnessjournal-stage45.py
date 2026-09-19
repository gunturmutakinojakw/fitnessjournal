# === Stage 45: Add restore from backup with validation ===
# Project: FitnessJournal
import json
import os

def restore_backup(backup_path, target_path, validate=True):
    """Restore a JSON backup to target_path with optional validation."""
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    with open(backup_path, 'r') as f:
        data = json.load(f)
    if validate and not isinstance(data, dict):
        raise ValueError(f"Backup must be a JSON object, got {type(data).__name__}")
    if validate and 'entries' not in data:
        raise ValueError("Backup missing required 'entries' key")
    with open(target_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Backup restored: {backup_path} -> {target_path}")
