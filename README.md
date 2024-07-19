# README: Project practise_misc_things_app

To use the Things URL Scheme in Python, you can use the `webbrowser` module to open the Things URL and send commands to the Things app. Here's a step-by-step guide on how to do this:

1. **Import the Necessary Libraries**: You'll need `webbrowser` to open the Things URL and `urllib.parse` to properly encode the URLs.

2. **Construct the URL**: Create the Things URL based on the command you want to execute. Make sure to URL encode the parameters correctly.

3. **Open the URL**: Use `webbrowser.open` to execute the command by opening the URL.

Here's an example of how to create a new to-do in Things using Python:

```python
import webbrowser
import urllib.parse

# Define the base URL for the Things URL Scheme
base_url = "things:///add"

# Define the parameters for the to-do
params = {
    "title": "Buy milk",
    "notes": "High fat",
    "when": "today"
}

# Encode the parameters
encoded_params = '&'.join([f"{key}={urllib.parse.quote(value)}" for key, value in params.items()])

# Construct the full URL
full_url = f"{base_url}?{encoded_params}"

# Open the URL to execute the command
webbrowser.open(full_url)
```

In this example, we are creating a new to-do with the title "Buy milk", notes "High fat", and a due date set to today.

### Additional Examples

#### Create a Project with To-Dos

```python
import webbrowser
import urllib.parse
import json

# Define the base URL for the Things JSON command
base_url = "things:///json"

# Define the project and to-dos in JSON format
data = [
    {
        "type": "project",
        "attributes": {
            "title": "Go Shopping",
            "items": [
                {
                    "type": "to-do",
                    "attributes": {
                        "title": "Bread"
                    }
                },
                {
                    "type": "to-do",
                    "attributes": {
                        "title": "Milk"
                    }
                }
            ]
        }
    }
]

# Convert the data to JSON string and URL encode it
encoded_data = urllib.parse.quote(json.dumps(data))

# Construct the full URL
full_url = f"{base_url}?data={encoded_data}"

# Open the URL to execute the command
webbrowser.open(full_url)
```

In this example, a project named "Go Shopping" with two to-dos "Bread" and "Milk" is created.

### Handling Authentication

If your command requires an authorization token, you can include it as a parameter:

```python
import webbrowser
import urllib.parse

# Define the base URL for the Things URL Scheme
base_url = "things:///add"

# Define the parameters for the to-do, including the auth-token
params = {
    "title": "Book flights",
    "auth-token": "YOUR_AUTH_TOKEN_HERE"
}

# Encode the parameters
encoded_params = urllib.parse.urlencode(params)

# Construct the full URL
full_url = f"{base_url}?{encoded_params}"

# Open the URL to execute the command
webbrowser.open(full_url)
```

### Conclusion

Using the Things URL Scheme in Python is straightforward. By constructing the appropriate URLs and opening them with the `webbrowser` module, you can automate the creation of to-dos, projects, and more in the Things app. Just make sure to handle URL encoding properly and include the necessary parameters for your commands.

[chatgpt link](https://chatgpt.com/share/cb2615ab-acff-457d-9ced-f4fe152e018f)
