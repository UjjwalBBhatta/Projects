from src.add_custom_folder import add_custom_folder
from src.folder_checker import check_and_create_folders
from src.organizer import organize_files_by_extension
from src.set_creator import create_sets
from src.logger import log
import json
import pathlib
def main():
    """The main function to run the file organizer."""
    folder_path = input("Enter the path of the folder to organize (leave empty for current directory): ").strip()
    if not folder_path:
        folder_path = pathlib.Path.cwd()
    else:
        folder_path = pathlib.Path(folder_path)

    file_types = create_sets(folder_path)
    log(f"Detected file types: {file_types}")

    def create_missing_folders_callback(base_path, missing_folders):
        for folder in missing_folders:
            try:
                (base_path / folder).mkdir(parents=True, exist_ok=True)
                log(f"Created missing folder: {folder}")
            except Exception as e:
                log(f"Error creating folder '{folder}': {e}")

    all_folders_exist = check_and_create_folders(folder_path, file_types, create_missing_folders_callback)
    if not all_folders_exist:
        log("Some required folders were missing and have been created.")

    try:
        with open('folder_map.json', 'r') as f:
            folder_map = json.load(f)
    except Exception as e:
        log(f"Error loading folder_map.json: {e}")
        return

    organize_files_by_extension(folder_path, folder_map)
    log("File organization complete.")
    add_custom = input("Do you want to add a custom folder mapping? (y/n): ").strip().lower()
    if add_custom == 'y':
        add_custom_folder()
if __name__ == "__main__":
    main()



