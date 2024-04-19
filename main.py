import flet as ft


class ToDo:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height=450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'ToDo App'
        self.main_page()

    def main_page(self):
        pass

ft.app(target=ToDo)
        