# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: FitnessJournal
import re


def validate_username(username):
    """Validates a fitness journal username."""
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters.")
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValueError("Username can only contain letters, numbers, and underscores.")
    return username


def validate_date(date_string):
    """Validates a date string in YYYY-MM-DD format."""
    if not date_string or len(date_string) != 10:
        raise ValueError("Date must be in YYYY-MM-DD format.")
    try:
        year, month, day = date_string[:4], date_string[5:7], date_string[8:10]
        return int(year), int(month), int(day)
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")


def validate_integer(value):
    """Validates that a value is an integer within a given range."""
    if not isinstance(value, int) or value < 1 or value > 10000:
        raise ValueError("Value must be an integer between 1 and 10000.")
    return value


def validate_short_text(text, max_length=50):
    """Validates that a text is not empty and does not exceed a maximum length."""
    if not text or len(text) > max_length:
        raise ValueError(f"Text must not be empty and must be at most {max_length} characters.")
    return text
