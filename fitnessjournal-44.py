# === Stage 44: Add backup creation for the data file ===
# Project: FitnessJournal
def backup(self):
        """Create a timestamped backup of the data file."""
        if not self.data_file:
            return
        backup_dir = "backups"
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"fitness_journal_{timestamp}.json")
        try:
            shutil.copy2(self.data_file, backup_path)
            print(f"Backup saved: {backup_path}")
        except Exception as e:
            print(f"Backup failed: {e}")
