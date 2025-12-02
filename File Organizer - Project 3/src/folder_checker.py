import json
from pathlib import Path

def check_and_create_folders(folder_path, file_types, create_missing_callback=None):
    """
    Checks if folders for the required file types exist inside folder_path
    based on folder_map.json. If any required folder is missing and a
    create_missing_callback is provided, it will call that callback.

    Returns:
        True if all required folders exist (after creation if callback used),
        False if there was an error or folder_map is empty.
    """
    folder_path = Path(folder_path)

    try:
        with open('folder_map.json', 'r') as f:
            folder_map = json.load(f)
    except FileNotFoundError:
        print("folder_map.json not found.")
        return False
    except json.JSONDecodeError:
        print("Error: folder_map.json is not a valid JSON file.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    if not folder_map:
        print("folder_map.json is empty. No mappings defined.")
        return False

    # Determine which folder names are needed for the given file_types
    required_folders = set()
    for ftype in file_types:
        for folder_name, extensions in folder_map.items():
            if ftype in extensions:
                required_folders.add(folder_name)

    if not required_folders:
        print("No matching folder mappings found for these file types.")
        return False

    # Check which required folders exist on disk
    missing_folders = [folder for folder in required_folders if not (folder_path / folder).exists()]

    if missing_folders:
        print(f"Missing folders: {missing_folders}")
        if create_missing_callback:
            create_missing_callback(folder_path, missing_folders)
        else:
            print("No folder creation callback provided.")
            return False

    return True
