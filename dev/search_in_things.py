"""Function to Add tasks to Things App"""
import webbrowser
import urllib.parse

def search_in_things(query=""):
    """
    Search in the Things app for the given query.

    Parameters:
    - query: (str) The search query (optional).

    Example:
    search_in_things("shipping address")
    """
    base_url = "things:///search"

    if query:
        encoded_query = urllib.parse.quote(query)
        full_url = f"{base_url}?query={encoded_query}"
    else:
        full_url = base_url  # Show the search screen without a query

    webbrowser.open(full_url)

search_in_things("grocery")
