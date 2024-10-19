"""Function to Show a list, area, project, or to-do in the Things app"""
import webbrowser
import urllib.parse

def show_in_things(params):
    """
    Show a list, area, project, or to-do in the Things app.

    Parameters:
    - id: (str) ID of the list, area, project, or to-do to show.
    - query: (str) The name of an area, project, tag, or a built-in list (optional).
    - filter: (str) Comma-separated tags to filter by.

    Example:
    show_in_things({"id": "today"})

    show_in_things({"query": "Vacation", "filter": "Errand"})
    """
    base_url = "things:///show"

    encoded_params = "&".join([f"{key}={urllib.parse.quote(str(value))}" for key, value in params.items()])
    full_url = f"{base_url}?{encoded_params}"
    webbrowser.open(full_url)

if __name__ == "__main__":
    show_in_things({"id": "today"})
