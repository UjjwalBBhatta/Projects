# Web Scraper

A flexible, configuration-driven web scraper built with Python.

## Features
- Scrape any website by providing URL
- Multiple scraping modes:
  - Links (extract all URLs)
  - Headings (h1-h6)
  - Paragraphs
  - Custom tags with optional class filtering
- Export to CSV
- Interactive CLI
- Extensible via JSON configuration

## Architecture
```
web-scraper/
├── src/
│   ├── get_html.py           # HTTP requests
│   ├── html_converter.py     # HTML parsing
│   ├── map_user_input.py     # Configuration & UX
│   ├── scraper.py            # Scraping logic
│   └── data_storer.py        # CSV export
├── html_map.json             # Scraping configurations
└── main.py                   # Entry point
```

## Technologies
- Python 3.x
- BeautifulSoup4 (HTML parsing)
- requests (HTTP)
- csv, pathlib (data handling)

## Installation
```bash
pip install beautifulsoup4 requests
python main.py
```

## Usage
1. Run the scraper
2. Enter target URL
3. Select what to scrape:
   - Links (all `<a>` tags)
   - Headings (h1-h6)
   - Paragraphs
   - Custom (specify tag + class)
4. Data saved to `data/{type}.csv`

## Example
```bash
Enter URL: https://example.com
What do you want to scrape?
1. links - All <a> tags with href
2. headings - All h1–h6 headings
3. paragraphs - All <p> tags
4. custom - User-defined tag
Enter option: 1

Saved 47 rows to data/links.csv
```

## Extending
Add new scraping patterns to `html_map.json`:
```json
{
  "images": {
    "description": "All images",
    "tag": "img",
    "attributes": ["src", "alt"],
    "text": false
  }
}
```

## Future Improvements
- Rate limiting for multiple pages
- User-Agent headers
- Pagination support
- Export to JSON/Excel
- Scheduling/automation

## What I Learned
- Web scraping with BeautifulSoup
- Modular architecture design
- Configuration-driven development
- Error handling best practices
- CSV data export