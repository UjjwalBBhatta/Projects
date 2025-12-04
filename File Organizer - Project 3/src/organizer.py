import pathlib
import shutil
from src.logger import log
def organize_files_by_extension(folder_path, folder_map):
    """This function organizes files in the given folder_path into subfolders.
    Files are moved into subfolders based on their extensions as defined in folder_map."""
    folder_path = pathlib.Path(folder_path)

    try:
        for file in folder_path.iterdir():
            if file.is_file():
                file_extension = file.suffix.lower()
                target_folder = None

                for folder_name, extensions in folder_map.items():
                    if file_extension in extensions:
                        target_folder = folder_name
                        break

                if target_folder:
                    destination = folder_path / target_folder / file.name
                    try:
                        shutil.move(str(file), str(destination))
                        log(f"Moved file '{file.name}' to folder '{target_folder}'.")
                    except Exception as e:
                        log(f"Error moving file '{file.name}' to folder '{target_folder}': {e}")
                else:
                    log(f"No target folder found for file '{file.name}' with extension '{file_extension}'.")
    except Exception as e:
        log(f"An error occurred while organizing files: {e}")

    