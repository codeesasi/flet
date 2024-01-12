import flet as ft

def main(page):
    page.title = "Image Viewer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def load_images(e):
        image_paths = ["Imageviewer/aff_1.jpg", "Imageviewer/aff_2.jpg"]

        # Create a list to store image elements
        image_elements = []

        # Create Image elements for each image path
        for image_path in image_paths:
            image_element = ft.Image(src=image_path, width=400, height=550)
            image_elements.append(image_element)

        # Function to handle zoom in
        def zoom_in(zoom_event):
            nonlocal image_elements
            for image_element in image_elements:
                image_element.width += 50
                image_element.height += 50

        # Function to handle zoom out
        def zoom_out(zoom_event):
            nonlocal image_elements
            for image_element in image_elements:
                image_element.width -= 50
                image_element.height -= 50

        # Create zoom buttons
        zoom_in_button = ft.ElevatedButton("Zoom In", on_click=zoom_in)
        zoom_out_button = ft.ElevatedButton("Zoom Out", on_click=zoom_out)

        # Create a card to display the images and zoom buttons
        image_card = ft.Card(
            content=ft.Column(
                [
                    ft.Text("Image Viewer", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row(image_elements, spacing=10),  # Display the images
                    ft.Row([zoom_in_button, zoom_out_button], spacing=10)  # Zoom buttons
                ],
                spacing=10
            )
        )

        # Add the card to the page
        page.add(image_card)

    # Button to trigger image loading
    load_button = ft.ElevatedButton("Load Images", on_click=load_images)

    # Add the button to the page
    page.add(ft.Column([load_button]))

# Start the app
ft.app(target=main)
