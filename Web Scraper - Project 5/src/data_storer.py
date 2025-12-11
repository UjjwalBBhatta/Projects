import csv
from pathlib import Path


def save_to_csv(rows, filename, out_dir="data"):
    """
    Save a list of dicts to a CSV file.

    Args:
        rows (list[dict]): List of dictionaries (each is one row).
        filename (str): Output filename, e.g. 'links.csv'.
        out_dir (str): Directory to store CSV files (default: 'data').
    """
    if not rows:
        print("No data to save.")
        return

    # Ensure output directory exists
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Full path to CSV
    file_path = out_path / filename

    # Determine CSV columns from keys of the first row
    fieldnames = list(rows[0].keys())

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Saved {len(rows)} rows to {file_path}")
    except OSError as e:
        print(f"Error writing CSV file: {e}")
