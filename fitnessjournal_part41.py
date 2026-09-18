# === Stage 41: Add plain text import for a simple line-based format ===
# Project: FitnessJournal
def read_lines(path):
    with open(path) as f:
        return f.read().splitlines()

def write_lines(path, lines):
    with open(path, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def load_json(path):
    import json
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    import json
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
