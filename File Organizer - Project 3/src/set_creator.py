import pathlib

def create_sets(folder_path):
    """This module is made to create a pythion set of file extensions inside the folder path provided by the user.
    If no folder path is provided, it defaults the cwd"""
    set_of_extensions = set()
    for file in pathlib.Path(folder_path).iterdir():
        if file.is_file():
            extension = file.suffix.lower()
            if extension:
                set_of_extensions.add(extension)
    return set_of_extensions

            