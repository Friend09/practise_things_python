"""Function to Add tasks to Things App"""
import webbrowser
import urllib.parse

def add_tasks_to_things(tasks):
    """
    Add tasks to the Things app using its URL scheme.

    This function allows you to add individual or multiple to-dos into the Things app with a variety of parameters like titles, notes, tags, when (schedule), list, and list-id.

    Parameters:
    tasks (list of dicts): Each task should be a dictionary containing the task parameters like title, notes, when, list, etc.
        - title: (str) The title of the to-do. Ignored if 'titles' is also specified.
        - titles: (list of str) Multiple to-do titles. If provided, the other parameters will be applied to all created to-dos.
        - notes: (str) Notes for the to-do.
        - when: (str) When to schedule the to-do (e.g., 'today', 'tomorrow', 'evening@6pm').
        - deadline: (str) Deadline date for the task.
        - tags: (str) Comma-separated tag names to apply to the task.
        - checklist-items: (list of str) List of checklist items (separated by new lines).
        - list: (str) The name of the project or area to add the to-do to. Ignored if 'list-id' is specified.
        - list-id: (str) The ID of the project or area to add the to-do to.
        - heading: (str) Title of a heading within a project.
        - heading-id: (str) ID of a heading within a project.
        - completed: (bool) Set the to-do as completed (default: False).
        - canceled: (bool) Set the to-do as canceled (default: False).
        - show-quick-entry: (bool) Show the quick entry dialog instead of adding the to-do (default: False).
        - reveal: (bool) Whether to show the newly created to-do (default: False).

    Example Usage:

    1. Adding a single to-do with basic parameters:

        add_tasks_to_things([
            {
                "title": "Buy Milk",
                "notes": "Low fat",
                "when": "today",
                "tags": "Errand"
            }
        ])

    2. Adding multiple to-dos at once to a project:

        add_tasks_to_things([
            {
                "titles": ["Milk", "Bread", "Cheese"],
                "list": "Shopping"
            }
        ])

    3. Adding a to-do with a reminder at a specific time:

        add_tasks_to_things([
            {
                "title": "Collect dry cleaning",
                "when": "evening@6pm",
                "list": "Errands"
            }
        ])

    4. Adding a to-do with a checklist:

        add_tasks_to_things([
            {
                "title": "Prepare for meeting",
                "checklist-items": ["Review notes", "Create presentation", "Send invite"],
                "when": "tomorrow",
                "list": "Work"
            }
        ])

    5. Scheduling a task in a specific area by ID:

        add_tasks_to_things([
            {
                "title": "Call Doctor",
                "when": "next monday",
                "list-id": "3052219D-8039-43D0-8654-AE1E20BE4F56"
            }
        ])

    Notes:
    - You can add up to 250 items within a 10-second period.
    - If 'when' or 'list-id' is not specified, the to-do will be added to the inbox.
    """
    base_url = "things:///"  # Things URL scheme
    task_action = "add"  # Action to add a task

    for task in tasks:
        # Handle multiple titles case (create multiple to-dos at once)
        if "titles" in task:
            task["titles"] = "%0a".join(task["titles"])  # Encode titles with new lines

        # Handle checklist items
        if "checklist-items" in task:
            task["checklist-items"] = "%0a".join(task["checklist-items"])  # Encode checklist items

        # Encode task parameters for the Things URL scheme
        encoded_params = "&".join(
            [f"{key}={urllib.parse.quote(str(value))}" for key, value in task.items()]
        )

        # Construct the full URL
        full_url = f"{base_url}{task_action}?{encoded_params}"

        # Open the URL to add the task to Things
        webbrowser.open(full_url)

if __name__ == "__main__":
    tasks = [
        {
            "title": "Machine Learning Project - 100 Days of ML Code",
            "when": "today",
            # "deadline": "2024-10-22",
            "tags": "machine learning",
            "notes": "https://github.com/Avik-Jain/100-Days-Of-ML-Code"
        },
    ]

    add_tasks_to_things(tasks)
