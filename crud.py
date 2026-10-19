from file import load_notes, save_notes

def create_note(title, content, tags):
    notes = load_notes()
    
    if title in notes:
        return False, f"Error: Note '{title}' already exists."
    
    notes[title] = {
        "content": content or "",
        "tags": tags.split(",") if tags else []
    }
    
    save_notes(notes)
    return True, f"Created note: '{title}'"

def read_note(title):
    notes = load_notes()
    return notes.get(title)

def update_note(title, content, tags):
    notes = load_notes()
    
    if title not in notes:
        return False, f"Error: Note '{title}' not found."
    
    if content:
        notes[title]["content"] = content
    if tags:
        notes[title]["tags"] = tags.split(",")
        
    save_notes(notes)
    return True, f"Updated note: '{title}'"

def delete_note(title):
    notes = load_notes()
    
    if title in notes:
        del notes[title]
        save_notes(notes)
        return True, f"Deleted note: '{title}'"
        
    return False, f"Error: Note '{title}' not found."

def list_notes(tag=None, keyword=None):
    notes = load_notes()
    filtered_notes = {}
    
    for title, data in notes.items():
        match = True
        
        if tag and tag not in data.get("tags", []):
            match = False
            
        if keyword and keyword.lower() not in data.get("content", "").lower():
            match = False
            
        if match:
            filtered_notes[title] = data
            
    return filtered_notes