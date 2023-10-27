from characters.race import Elf, Dwarf, Orc
import flet as ft
from time import sleep

available = "Available Races"


def main(page: ft.Page):
    page.add(ft.Text(available))
    page.add(ft.Text(Elf.__str__(Elf())))
    page.add(ft.Text(Elf.__str__(Dwarf())))
    page.add(ft.Text(Elf.__str__(Orc())))
    page.title = "RPG GAME BY KONRAD!"

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.STAR, label="Elf"),
            ft.NavigationDestination(icon=ft.icons.STAR, label="Dwarf"),
            ft.NavigationDestination(icon=ft.icons.STAR, label="Orc"),
        ]
    )
    page.add(ft.Text("CHOSE!!"))


ft.app(target=main)
