"""Function to Add a project to Things App"""
import webbrowser
import urllib.parse

def add_project_to_things(params):
    """
    Adds a project to the Things app.

    Parameters (all optional):
    - title: (str) The title of the project.
    - notes: (str) Notes for the project.
    - when: (str) Schedule (e.g., 'today', 'tomorrow', 'next week').
    - deadline: (str) Deadline for the project.
    - tags: (str) Comma-separated tags.
    - area: (str) The name of the area to add the project to.
    - area-id: (str) The ID of the area to add the project to.
    - to-dos: (list of str) Checklist of to-dos inside the project.
    - completed: (bool) Set the project as completed.
    - reveal: (bool) Navigate into the newly created project.

    Example:
    add_project_to_things({
        "title": "Build Treehouse",
        "when": "today",
        "to-dos": ["Get wood", "Hire helper", "Build"],
        "tags": "Home,DIY"
    })
    """
    base_url = "things:///add-project"
    if 'to-dos' in params:
        params['to-dos'] = "%0a".join(params['to-dos'])  # Encode to-dos with new lines

    encoded_params = "&".join([f"{key}={urllib.parse.quote(str(value))}" for key, value in params.items()])
    full_url = f"{base_url}?{encoded_params}"
    webbrowser.open(full_url)

if __name__ == "__main__":
    add_project_to_things({
    "title": "Plan Birthday Party",
    "when": "next week",
    "tags": "Family,Event",
    "to-dos": ["Send invites", "Order cake", "Decorations"]
})
