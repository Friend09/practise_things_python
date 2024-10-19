"""Function to Update a To do in Things App"""
import webbrowser
import urllib.parse

def update_todo_in_things(id, params):
    """
    Update an existing to-do in the Things app.

    Parameters:
    - id: (str) The ID of the to-do to update (required).
    - title: (str) Update the title.
    - notes: (str) Replace notes with this text.
    - prepend-notes: (str) Add text before existing notes.
    - append-notes: (str) Add text after existing notes.
    - when: (str) Schedule (e.g., 'today', 'tomorrow').
    - tags: (str) Comma-separated tags to apply to the to-do.
    - checklist-items: (list of str) Replace checklist items.
    - append-checklist-items: (list of str) Add checklist items.
    - deadline: (str) Update the deadline.

    Example:
    update_todo_in_things("4BE64FEA-8FEF-4F4F-B8B2-4E74605D5FA5", {
        "title": "Buy bread",
        "append-notes": "Wholemeal bread",
        "append-checklist-items": ["Buy eggs", "Buy butter"]
    })
    """
    base_url = "things:///update"
    params['id'] = id  # Include the ID in parameters

    # Handle checklist items if provided
    if "checklist-items" in params:
        params["checklist-items"] = "%0a".join(params["checklist-items"])
    if "append-checklist-items" in params:
        params["append-checklist-items"] = "%0a".join(params["append-checklist-items"])

    encoded_params = "&".join([f"{key}={urllib.parse.quote(str(value))}" for key, value in params.items()])
    full_url = f"{base_url}?{encoded_params}"
    webbrowser.open(full_url)

if __name__ == "__main__":
    update_todo_in_things("4BE64FEA-8FEF-4F4F-B8B2-4E74605D5FA5", {
    "title": "Buy bread",
    "when": "today",
    "append-notes": "Wholemeal",
    "append-checklist-items": ["Check for discounts"]
})
