from src.get_html import get_html
from src.html_converter import convert_html_to_soup
from src.map_user_input import get_user_config
from src.scraper import scrape_with_config
from src.data_storer import save_to_csv


def main():
    url = input("Enter URL to scrape: ").strip()
    if not url:
        print("No URL provided.")
        return

    html = get_html(url)
    if html is None:
        print("Failed to fetch HTML from the URL.")
        return

    soup = convert_html_to_soup(html)
    if soup is None:
        print("Failed to parse HTML.")
        return

    config = get_user_config()
    if config is None:
        print("Failed to load scraping configuration.")
        return

    rows = scrape_with_config(soup, config)
    if not rows:
        print("No data found with the selected configuration.")
        return

    # filename based on key, e.g. links.csv, headings.csv, custom.csv
    key = config.get("key", "output")
    filename = f"{key}.csv"

    save_to_csv(rows, filename)


if __name__ == "__main__":
    main()
