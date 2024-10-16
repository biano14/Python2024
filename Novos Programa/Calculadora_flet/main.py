import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    alignment,
)

# Definindo os botões da calculadora
buttons_config = [
    {"label": "AC", "text_color": colors.BLACK, "bg_color": "#A9A9A9"},
    {"label": "⌫", "text_color": colors.BLACK, "bg_color": "#A9A9A9"},
    {"label": "%", "text_color": colors.BLACK, "bg_color": "#A9A9A9"},
    {"label": "/", "text_color": colors.BLACK, "bg_color": colors.DEEP_ORANGE},
    {"label": "7", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "8", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "9", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "*", "text_color": colors.BLACK, "bg_color": colors.DEEP_ORANGE},
    {"label": "4", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "5", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "6", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "-", "text_color": colors.BLACK, "bg_color": colors.DEEP_ORANGE},
    {"label": "1", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "2", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "3", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "+", "text_color": colors.BLACK, "bg_color": colors.DEEP_ORANGE},
    {"label": "0", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": ",", "text_color": colors.WHITE, "bg_color": "#1C1C1C"},
    {"label": "=", "text_color": colors.BLACK, "bg_color": colors.LIGHT_GREEN_ACCENT_700},
]

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#000"
    page.window_resizable = False
    page.window_width = 350
    page.window_height = 520
    page.window_position = "center"
    page.window_always_on_top = True

    display = ft.Text(value="0", color="#ffffff", size=40)
    result_shown = False

    def compute(expression):
        try:
            return str(eval(expression))
        except ZeroDivisionError:
            return "Erro"
        except Exception as e:
            return f"Erro: {str(e)}"

    def button_click(event):
        nonlocal result_shown
        current_value = display.value if display.value != "0" else ""
        clicked_value = event.control.content.value

        if clicked_value.isdigit():
            if result_shown:
                current_value = ""
                result_shown = False
            current_value += clicked_value
        elif clicked_value == "AC":
            current_value = "0"
        elif clicked_value == "⌫":
            current_value = current_value[:-1] if current_value[:-1] else "0"
        else:
            if current_value and current_value[-1] in ["/", "*", "-", "+", ","]:
                current_value = current_value[:-1]
            current_value += clicked_value
            if current_value[-1] in ["=", "%"]:
                current_value = compute(current_value[:-1])
                result_shown = True

        display.value = current_value
        display.update()

    display_row = ft.Row(
        controls=[display],
        width=390,
        alignment="end",
    )

    buttons = [
        ft.Container(
            content=ft.Text(value=btn["label"], color=btn["text_color"], size=20, expand=1),
            width=148 if btn["label"] == "=" else 74,
            height=70,
            bgcolor=btn["bg_color"],
            border_radius=25,
            alignment=ft.alignment.center,
            on_click=button_click,
        ) for btn in buttons_config
    ]

    keyboard_row = ft.Row(
        controls=buttons,
        width=390,
        wrap=True,
        alignment="center",
        spacing=5,
    )

    page.add(display_row, keyboard_row)

ft.app(target=main)
