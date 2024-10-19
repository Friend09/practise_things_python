"""Retrieve the version of the Things app and URL scheme."""
import webbrowser
import urllib.parse

def get_things_version():
    """
    Retrieve the version of the Things app and URL scheme.

    Example:
    get_things_version()
    """
    base_url = "things:///version"
    webbrowser.open(base_url)

get_things_version()
