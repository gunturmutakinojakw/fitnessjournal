# === Stage 20: Add duplicate detection for newly created records ===
# Project: FitnessJournal
def detect_duplicates(records, new_record):
    """Detect if a new record is a duplicate of any existing record.
    
    Args:
        records: List of existing records (each is a dict with 'date', 'exercise', 'sets', 'weight', 'notes')
        new_record: Dict representing the new record to check
    
    Returns:
        List of tuples (existing_record, similarity_score) where similarity_score > 0.5 indicates a potential duplicate
    """
    duplicates = []
    
    for existing in records:
        if existing['date'] != new_record['date']:
            continue
        
        # Calculate similarity based on exercise name and sets
        exercise_sim = calculate_string_similarity(existing['exercise'], new_record['exercise'])
        sets_sim = calculate_float_similarity(existing['sets'], new_record['sets'])
        
        # Weight similarity only if weight is present in both
        if 'weight' in existing and 'weight' in new_record:
            weight_sim = calculate_float_similarity(existing['weight'], new_record['weight'])
        else:
            weight_sim = 0.5  # No weight to compare, assume partial similarity
        
        # Calculate overall similarity score
        similarity = (exercise_sim + sets_sim + weight_sim) / 3
        
        if similarity > 0.5:
            duplicates.append((existing, similarity))
    
    return duplicates

def calculate_string_similarity(str1, str2):
    """Calculate string similarity using character overlap ratio."""
    if not str1 or not str2:
        return 0.0
    
    # Use simple character overlap calculation
    intersection = sum(1 for c in str1 if c in str2)
    union = len(str1) + len(str2) - intersection
    return intersection / union if union > 0 else 0.0

def calculate_float_similarity(val1, val2):
    """Calculate similarity between two float values (0-1 scale).
    
    Returns 1.0 if values are equal, 0.5 if within 10% relative difference, 0.0 otherwise.
    """
    if val1 == val2:
        return 1.0
    
    if val1 == 0 and val2 == 0:
        return 1.0
    
    # Use relative difference
    max_val = max(abs(val1), abs(val2))
    if max_val == 0:
        return 0.0
    
    diff = abs(val1 - val2) / max_val
    
    if diff < 0.1:
        return 1.0
    elif diff < 0.3:
        return 0.5
    else:
        return 0.0
