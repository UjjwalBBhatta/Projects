from bs4 import BeautifulSoup


def _extract_from_tag(tag, config):
    """
    Extract data from a single BeautifulSoup tag using config rules.
    Returns a dict (one row for CSV).
    """
    row = {}

    # Add tag name and class/id info (optional but useful)
    row["tag"] = tag.name
    row["class"] = " ".join(tag.get("class", [])) if tag.has_attr("class") else ""
    row["id"] = tag.get("id", "")

    # Text content
    if config.get("text", False):
        row["text"] = tag.get_text(strip=True)

    # Attributes defined in config["attributes"]
    for attr in config.get("attributes", []):
        row[attr] = tag.get(attr, "")

    return row


def scrape_with_config(soup: BeautifulSoup, config: dict):
    """
    Scrape data from a BeautifulSoup object using a config dict.

    Args:
        soup (BeautifulSoup): Parsed HTML.
        config (dict): Config from map_user_input.get_user_config() / html_map.json.

    Returns:
        list[dict]: Extracted rows ready to be stored in CSV.
    """
    results = []

    # Case 1: multiple tags (e.g., headings h1–h6)
    if "tags" in config and config["tags"]:
        for tag_name in config["tags"]:
            tags = soup.find_all(tag_name)
            for t in tags:
                results.append(_extract_from_tag(t, config))
        return results

    # Case 2: single tag, with optional class filter
    tag_name = config.get("tag")
    css_class = config.get("class")

    if not tag_name:
        print("Config missing 'tag' or 'tags'; nothing to scrape.")
        return results

    if css_class:
        tags = soup.find_all(tag_name, class_=css_class)
    else:
        tags = soup.find_all(tag_name)

    for t in tags:
        results.append(_extract_from_tag(t, config))

    return results
