# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: FitnessJournal
import json
from pathlib import Path

def archive_records(records, archive_dir="archive"):
    p = Path(archive_dir)
    p.mkdir(parents=True, exist_ok=True)
    archived = []
    for r in records:
        if r["done"] or r["date"] < "2025-01-01":
            entry = {
                "name": r["name"],
                "date": r["date"],
                "sets": r["sets"],
                "done": r["done"],
                "pr": r["pr"],
            }
            fname = p / f"{r['name'].replace(' ', '_')}_{r['date']}.json"
            fname.write_text(json.dumps(entry, indent=2))
            archived.append(r["name"])
    return archived

def restore_records(archive_dir="archive", records=None):
    if records is None:
        records = []
    p = Path(archive_dir)
    if not p.exists():
        return records
    for f in sorted(p.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
            records.append(entry)
        except Exception:
            pass
    return records
