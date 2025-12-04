# Smart File Organizer

A modular Python CLI tool that automatically organizes files by extension with customizable folder mappings and comprehensive logging.

## Features

### Core Functionality
- **Automatic Extension Detection**: Scans folder and identifies all file types present
- **Smart Folder Creation**: Only creates folders needed for detected file types
- **Customizable Mappings**: JSON-based configuration for folder → extension mappings
- **Move Operations**: Safely moves files to appropriate folders using shutil
- **Comprehensive Logging**: All operations logged with timestamps to activity.log

### User Customization
- **Add Custom Mappings**: Interactive prompt to add new folder/extension associations
- **Validation**: Prevents duplicate mappings and invalid extension formats
- **Flexible Input**: Works with specified path or current directory

## Architecture

### Module Structure
```
file-organizer/
├── main.py                    # Entry point, orchestrates workflow
├── organizer.py               # Core file moving logic
├── folder_checker.py          # Folder existence validation and creation
├── set_creator.py             # Extension detection from folder contents
├── add_custom_folder.py       # User customization interface
├── logger.py                  # Centralized logging system
├── folder_map.json            # Configuration: folder → extensions mapping
└── activity.log               # Operation history with timestamps
```

### Design Patterns
- **Callback Pattern**: Folder creation uses callback for separation of concerns
- **Configuration-Driven**: Behavior defined by JSON, not hardcoded
- **Single Responsibility**: Each module handles one aspect of the system

## How It Works

1. **Folder Selection**: User specifies target folder (or uses current directory)
2. **Extension Detection**: System scans folder and identifies all file types
3. **Folder Validation**: Checks which organization folders are needed and missing
4. **Folder Creation**: Creates only the folders needed for detected file types
5. **File Organization**: Moves each file to its designated folder based on mapping
6. **Optional Customization**: User can add new folder/extension mappings

## Installation
```bash
git clone https://github.com/yourusername/file-organizer
cd file-organizer
python main.py
```

## Usage
```bash
# Organize current directory
python main.py

# Organize specific folder
python main.py /path/to/folder
```

### Adding Custom Mappings

When prompted after organization:
```
Do you want to add a custom folder mapping? (y/n): y
Enter folder name: Projects
Enter extensions (comma-separated): .psd,.ai,.sketch
```

## Technologies

- **Python 3.x**
- **pathlib**: Cross-platform path handling
- **shutil**: Safe file operations
- **json**: Configuration persistence
- **datetime**: Timestamp logging

## Configuration

`folder_map.json` structure:
```json
{
  "Images": [".jpg", ".jpeg", ".png", ".gif"],
  "Documents": [".pdf", ".docx", ".txt"],
  "Videos": [".mp4", ".avi", ".mkv"]
}
```

## Logging

All operations logged to `activity.log`:
```
2025-12-05 14:23:15 - Detected file types: {'.jpg', '.pdf', '.mp4'}
2025-12-05 14:23:16 - Created folder: Images
2025-12-05 14:23:17 - Moved photo.jpg → Images/photo.jpg
```

## Roadmap (v2.0)

- [ ] Interactive menu system with home screen
- [ ] Display current folder and active mappings
- [ ] Bulk update extension mappings
- [ ] Undo functionality
- [ ] Dry-run mode (preview without moving)
- [ ] GUI interface
- [ ] Scheduled organization

## What I Learned

- **Modular Architecture**: Breaking complex systems into manageable, single-purpose modules
- **Callback Patterns**: Decoupling logic for flexibility and testability
- **JSON Configuration**: External configuration for user customization
- **Error Handling**: Validation and edge case management
- **Logging Best Practices**: Comprehensive operation tracking
- **User Experience Design**: Interactive prompts and feedback

## Contributing

Suggestions for v2.0 features welcome! Open an issue or PR.

## License

MIT