# utils.py

import json

def load_passwords(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def save_passwords(file_path, passwords):
    with open(file_path, 'w') as file:
        json.dump(passwords, file, indent=4)