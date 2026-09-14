# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: FitnessJournal
import re
from datetime import datetime

def parse_date(date_str):
    """Parse date strings in common formats with clear error messages.
    
    Supported formats: YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY, DD.MM.YYYY
    
    Args:
        date_str: Date string to parse
        
    Returns:
        datetime object or None if parsing fails
        
    Raises:
        ValueError: With descriptive message if date is invalid
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError(f"Invalid date input: {date_str!r}. Must be a non-empty string.")
    
    date_str = date_str.strip()
    
    # Try YYYY-MM-DD
    for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d.%m.%Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    raise ValueError(
        f"Unrecognized date format: {date_str!r}. "
        "Supported formats: YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY, DD.MM.YYYY"
    )
