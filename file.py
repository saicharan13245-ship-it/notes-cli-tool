import json
import config
import os
def load_notes():
    if not os.path.exists(config.notes_file):
        return {}
    with open(config.notes_file,"r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_notes(data):
    with open(config.notes_file,"w") as f:
        json.dump(data, f, indent=4)

