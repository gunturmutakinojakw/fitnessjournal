# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: FitnessJournal
def delete_entry(entry_id: str, confirm: bool = False) -> dict:
    """Delete a workout entry by ID.
    
    Args:
        entry_id: Unique identifier of the entry to delete.
        confirm: If True, prompt the user for confirmation before deletion.
        
    Returns:
        A dict with 'success' (bool) and 'message' (str) describing the result.
    """
    if not _is_valid_entry_id(entry_id):
        return {"success": False, "message": f"Entry '{entry_id}' not found."}
    
    if confirm:
        response = input(f"Are you sure you want to delete entry '{entry_id}'? (y/n): ")
        if response.lower() not in ('y', 'yes'):
            return {"success": False, "message": "Deletion cancelled by user."}
    
    # Remove the entry from the data store
    if entry_id in _entries:
        del _entries[entry_id]
        return {"success": True, "message": f"Entry '{entry_id}' deleted successfully."}
    
    return {"success": False, "message": f"Entry '{entry_id}' not found after re-check."}
