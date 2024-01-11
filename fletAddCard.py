# import flet as ft
# import requests

# def main(page: ft.Page):
#     page.window_width = 490
#     page.window_height = 844
    
#     def bitcoin_update(e):
#         #this function will be called when the button is clicked
#         response = requests.post("https://cevabooking.mytlx.com:1996/dev/getOVNumber")
#         if response.status_code == 200:
#             data = response.json()
#             txt = ft.Text(data)
#             page.scroll = "always"
#             page.add(txt)
#             page.update()
#         else:
#             txt = ft.Text(f"API Call Failed! Status Code: {response.status_code}")
#             page.add(txt)
#             page.update()

#     # show the detais where the button is clicked
#     basic_button = ft.ElevatedButton("call API..", on_click=bitcoin_update)
#     page.add(basic_button)


# ft.app(target=main, view=ft.AppView.FLET_APP)

import flet as ft

def main(page):
    page.title = "Card Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Create a list to hold the cards
    cards_list = []

    # Function to add a new card with a close button
    def add_card(e):
        new_card = ft.Card(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ACCOUNT_BALANCE),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                        autofocus=True,
                        
                    ),
                    ft.ElevatedButton("Close", on_click=lambda _: remove_card(new_card))
                    
                ],
            ),
        )
        cards_list.append(new_card)
        page.add(new_card)  # Directly add the new card to the page

    def remove_card(card):
        cards_list.remove(card)
        page.remove(card)

    # Create a button to add a new card
    add_card_button = ft.ElevatedButton("Add Card", on_click=add_card)

    # Add the list of cards and the button to the page
    page.add(ft.Column([*cards_list, add_card_button]))

# Start the app
ft.app(target=main)
