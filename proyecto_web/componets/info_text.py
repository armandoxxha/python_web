import reflex as rx
from proyecto_web.styles.styles import Spacer as Spacer
from proyecto_web.styles.colores import Color as Color
from proyecto_web.styles.colores import TextColor as TextColor
def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f"{ body}",
        font_size=Spacer.MEDIUM.value,
        color=TextColor.BODY.value
    )
