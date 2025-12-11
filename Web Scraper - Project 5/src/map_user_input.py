import json
from pathlib import Path

MAP_PATH = Path(__file__).resolve().parent.parent / "html_map.json"


def load_html_map():
    """Load HTML mapping configuration from html_map.json."""
    try:
        with open(MAP_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at: {MAP_PATH}")
    except json.JSONDecodeError as e:
        print(f"Error parsing html_map.json: {e}")
    return None


def ask_user_choice(html_map):
    """
    Ask the user what they want to scrape and return the key from html_map.
    """
    print("What do you want to scrape?")
    keys = list(html_map.keys())

    for idx, key in enumerate(keys, start=1):
        desc = html_map[key].get("description", "")
        print(f"{idx}. {key} - {desc}")

    while True:
        choice = input("Enter option number: ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        idx = int(choice)
        if 1 <= idx <= len(keys):
            return keys[idx - 1]
        else:
            print("Choice out of range. Try again.")


def get_user_config():
    """
    Load html_map and interactively get a configuration for scraping.

    Returns:
        dict | None: Configuration dict from html_map (possibly updated for 'custom').
    """
    html_map = load_html_map()
    if html_map is None:
        return None

    choice_key = ask_user_choice(html_map)
    config = html_map[choice_key].copy()
    config["key"] = choice_key  # remember which option was chosen

    # Handle custom case: ask for tag and optional class
    if choice_key == "custom":
        tag = input("Enter HTML tag to search for (e.g., div, span, a): ").strip()
        css_class = input("Enter class name to filter by (or leave blank): ").strip()

        config["tag"] = tag if tag else None
        config["class"] = css_class if css_class else None

    return config
