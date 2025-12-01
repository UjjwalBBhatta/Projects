import json

def add_custom_folder():
    """Ask user for a folder name and file types, then update folder_map.json."""
    folder_name = input("Enter the name of the custom folder to create: ").strip()
    filetypes_input = input("Enter the file types to include (separate by commas, e.g. .txt,.jpg): ").strip().lower()
    filetypes = [ftype.strip() for ftype in filetypes_input.split(',') if ftype.strip().startswith('.')]

    if not folder_name:
        print("Folder name cannot be empty.")
        return
    if not filetypes:
        print("No valid file types provided.")
        return

    try:
        with open('folder_map.json', 'r') as f:
            folder_map = json.load(f)
    except FileNotFoundError:
        folder_map = {}
    except json.JSONDecodeError:
        print("Error: folder_map.json is not a valid JSON file.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    if folder_name in folder_map:
        print(f"Folder name '{folder_name}' already exists. Please choose a different name.")
        return

    for ftype in filetypes:
        for existing_folder, existing_types in folder_map.items():
            if ftype in existing_types:
                print(f"File type '{ftype}' is already assigned to folder '{existing_folder}'. Please choose different file types.")
                return

    folder_map[folder_name] = filetypes

    try:
        with open('folder_map.json', 'w') as f:
            json.dump(folder_map, f, indent=4)
        print(f"Custom folder '{folder_name}' with file types {filetypes} added successfully.")
    except Exception as e:
        print(f"Error writing to folder_map.json: {e}")


