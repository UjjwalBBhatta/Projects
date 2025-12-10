import requests
def get_html(url):
    """This function returns the HTML content of the given URL.
    Args:
        url (str): The URL of the webpage to fetch.
        Returns:
        str: The HTML content of the webpage, or None if an error occurs."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
   
    
    
    

