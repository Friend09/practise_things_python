"""Function to Update an existing project in the Things app"""
import webbrowser
import urllib.parse

def update_project_in_things(id, params):
    """
    Update an existing project in the Things app.

    Parameters:
    - id: (str) The ID of the project to update (required).
    - title: (str) Update the title of the project.
    - notes: (str) Replace notes with this text.
    - prepend-notes: (str) Add text before existing notes.
    - append-notes: (str) Add text after existing notes.
    - when: (str) Schedule the project (e.g., 'today', 'tomorrow').
    - tags: (str) Comma-separated tags to apply to the project.
    - deadline: (str) Update the deadline.
    - add-tags: (str) Add additional tags to the project.

    Example:
    update_project_in_things("852763FD-5954-4DF9-A88A-2ADD808BD279", {
        "title": "Plan Birthday Party",
        "append-notes": "Don't forget the cake",
        "add-tags": "Important"
    })
    """
    base_url = "things:///update-project"
    params['id'] = id  # Include the project ID in parameters

    encoded_params = "&".join([f"{key}={urllib.parse.quote(str(value))}" for key, value in params.items()])
    full_url = f"{base_url}?{encoded_params}"
    webbrowser.open(full_url)
