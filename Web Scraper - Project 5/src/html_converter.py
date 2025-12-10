from bs4 import BeautifulSoup

def convert_html_to_soup(html_content):
    """Convert raw HTML into a BeautifulSoup object.
    Args:
        html_content (str): The HTML content to convert.
    Returns:
        BeautifulSoup | None: Parsed soup object, or None if an error occurs.
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    except Exception as e:
        print(f"An error occurred during HTML parsing: {e}")
        return None


def soup_to_text(soup):
    """Extract plain text from a BeautifulSoup object.
    Args:
        soup (BeautifulSoup): Parsed HTML soup.
    Returns:
        str: Plain text extracted from the HTML.
    """
    return soup.get_text(separator="\n", strip=True)
