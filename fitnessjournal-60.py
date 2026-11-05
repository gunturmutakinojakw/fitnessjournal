# === Stage 60: Add saved views for frequently used filters ===
# Project: FitnessJournal
class SavedView:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    def serialize(self):
        return {'name': self.name, 'filters': self.filters}

    @classmethod
    def deserialize(cls, data):
        return cls(data['name'], data['filters'])


class SavedViewManager:
    def __init__(self):
        self.saved_views = {}

    def add_saved_view(self, name, filters):
        self.saved_views[name] = SavedView(name, filters)
        return self.saved_views[name]

    def get_saved_view(self, name):
        return self.saved_views.get(name)

    def remove_saved_view(self, name):
        return self.saved_views.pop(name, None)

    def list_saved_views(self):
        return list(self.saved_views.keys())

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for name, view in self.saved_views.items():
                f.write(json.dumps(view.serialize()))
                f.write('\n')

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                self.saved_views[data['name']] = SavedView.deserialize(data)
