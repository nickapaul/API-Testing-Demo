import json

def read_json_to_dict(filepath):
    """Reads a JSON file and returns a dictionary."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filepath}.")
        return None
    
