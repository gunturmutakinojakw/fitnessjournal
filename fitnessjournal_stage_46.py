# === Stage 46: Add a schema version field and migration helper ===
# Project: FitnessJournal
SCHEMA_VERSION = 2


def migrate(data: dict) -> dict:
    """Apply schema migrations to the journal data."""
    if SCHEMA_VERSION not in data:
        data["schema_version"] = SCHEMA_VERSION
    if "weekly_summaries" not in data:
        data["weekly_summaries"] = []
    return data
