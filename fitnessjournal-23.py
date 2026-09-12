# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: FitnessJournal
def add_tag(entry, tag):
    """Add a tag to an entry if not already present."""
    if tag not in entry.get("tags", []):
        entry.setdefault("tags", []).append(tag)

def remove_tag(entry, tag):
    """Remove a tag from an entry if present."""
    if tag in entry.get("tags", []):
        entry["tags"].remove(tag)

def tag_summary(entries, tag):
    """Return a summary of entries filtered by the given tag."""
    filtered = [e for e in entries if tag in e.get("tags", [])]
    if not filtered:
        return {"tag": tag, "count": 0, "entries": []}
    return {
        "tag": tag,
        "count": len(filtered),
        "entries": filtered,
    }
