import flet as ft


class ToDo:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.GREY_800
        self.page.window_width = 350
        self.page.window_height=500
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'ToDo App'
        self.main_page()

    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls = [
                    ft.Checkbox(label='Tarefa 1', value=True)
                ]
            )

        )

    def main_page(self):
        input_task = ft.TextField(hint_text='Digite aqui um tarefa', expand=True)
        input_bar = ft.Row(
            controls=[
            input_task,
            ft.FloatingActionButton(icon=ft.icons.ADD)
            ]
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Em Andamento"),
                ft.Tab(text="Finalizados")
            ]
        )

        tasks = self.tasks_container()

        self.page.add(input_bar, tabs, tasks)

ft.app(target=ToDo)
        