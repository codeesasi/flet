import flet as ft

def main(page: ft.Page):
    page.add(
        ft.SelectionArea(
            content=ft.Column([ft.Text("Selectable text"), ft.Text("Also selectable")])
        )
    )
    page.add(ft.Text("Not selectable"))

ft.app(main)