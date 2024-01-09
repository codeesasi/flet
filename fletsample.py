import flet as ft
import requests
import json

def main(page):
    response = requests.get("https://www.google.com")
    # Convert the JSON data to a formatted string
    try:
        json_data = response.json() if response.status_code == 200 else {"StatusCode": f"API Call Failed! Status Code: {response.status_code}"}
        formatted_json = json.dumps(json_data, indent=4)
    except Exception as e:
        print(e)
        formatted_json = response.text

    # Display the entire JSON response
    page.theme_mode = ft.ThemeMode.DARK # change DARK to LIGHT to convert it to light mode 
    page.window_height = 400
    page.window_width = 500
    page.add(ft.Text(formatted_json, size=14))

ft.app(target=main)
