import flet as ft
import json

def main(page):
    page.title = "JSON Viewer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Function to load and display JSON content
    def load_json(e):
        try:
            with open("example.json", "r") as file:
                json_data = json.load(file)
                show_json_card(json_data)
        except Exception as ex:
            show_error_card(str(ex))

    # Function to display JSON content in a card
    def show_json_card(data):
        # Create a search input field
        search_input = ft.TextField(
            label="Search",
            width=400,
            height=30,
            text_align=ft.TextAlign.LEFT,
            on_change=lambda _: filter_json(search_input.value)
        )

        json_card = ft.Card(
            content=ft.Column(
                [
                    ft.Text("JSON Content", size=18, weight=ft.FontWeight.BOLD),
                    search_input,
                    ft.Text(json.dumps(data, indent=4), size=14)  # Display JSON content
                ],
                spacing=10,
                width=500,
            )
        )
        page.add(json_card)

    # Function to display error message in a card
    def show_error_card(error_message):
        error_card = ft.Card(
            content=ft.Column(
                [
                    ft.Text("Error", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.RED),
                    ft.Text(error_message, size=14)
                ],
                spacing=10
            )
        )
        page.add(error_card)

    # Function to filter JSON content based on search term
    def filter_json(search_term):
        # Retrieve the JSON content element
        json_content = page.get_element("json_content")
        if json_content:
            # Filter the JSON content based on the search term
            filtered_data = filter_json_recursive(search_term, original_json_data)
            json_content.value = json.dumps(filtered_data, indent=4)

    # Recursive function to filter JSON content
    def filter_json_recursive(search_term, data):
        if isinstance(data, list):
            return [filter_json_recursive(search_term, item) for item in data]
        elif isinstance(data, dict):
            return {key: filter_json_recursive(search_term, value) for key, value in data.items() if search_term.lower() in str(value).lower()}
        else:
            return data

    # Button to trigger JSON loading
    load_button = ft.ElevatedButton("Load JSON", on_click=load_json)

    # Add the button to the page
    page.add(ft.Column([load_button]))

    # Placeholder for the original JSON data
    original_json_data = None

# Start the app
ft.app(target=main)
