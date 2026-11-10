# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: FitnessJournal
def merge_imports(existing, new):
    norm = lambda s: s.strip().lower().replace(" ", "")
    merged = []
    seen = set()
    for line in existing + new:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = stripped.replace("from", " ").replace("import", " ").split()
        if parts and parts[0] in ("from", "import"):
            if parts[0] == "from":
                module = parts[1]
                names = [p for p in parts[2:] if p not in ("as",)]
                if module not in seen:
                    seen.add(module)
                    if names:
                        merged.append("from %s import %s" % (module, ", ".join(names)))
                    else:
                        merged.append("import %s" % module)
            else:
                names = [p for p in parts[1:] if p not in ("as",)]
                if not seen:
                    seen.add("import")
                    if names:
                        merged.append("import %s" % ", ".join(names))
    return merged
