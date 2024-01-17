import flet as ft
import openweb as ob


def main(page: ft.Page):
    page.title = "Click counter"

    def opengithub(e):
        ob.openweb(e=e, page=page, url="https://github.com/tct123")
    def openyt1(e):
        ob.openweb(e=e, page=page, url="https://youtube.com/@tc-diy")

    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        bgcolor=ft.colors.BLUE,
        actions=[
            ft.PopupMenuButton(
                items=[ft.PopupMenuItem(text="Github", on_click=opengithub),ft.PopupMenuItem(text="YouTube", on_click=openyt1)]
            )
        ],
    )
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def addfunc(e):
        text.value = str(int(text.value) + 1)
        page.update()

    text = ft.Text(str(0), text_align=ft.TextAlign.CENTER, size=32)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=addfunc
    )
    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[ft.Text("You pressed the button this many times:")],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    )
    page.add(
        ft.SafeArea(ft.Row(controls=[text], alignment=ft.MainAxisAlignment.CENTER))
    )


ft.app(main)
