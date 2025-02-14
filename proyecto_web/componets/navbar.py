import reflex as rx
from proyecto_web.styles.styles import Spacer as Spacer
from proyecto_web.styles.colores import Color as Color
import proyecto_web.styles.styles as styles
from proyecto_web.routes import Route
from proyecto_web.componets.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text.span(
                    "arma",
                    height="40px",
                    color=Color.PRIMARY.value
                ),
                rx.text.span(
                    "ndoxx",
                    height="40px",
                    color=Color.SECONDARY.value
                ),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        
        #float_button(),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Spacer.DEFAULT.value,
        padding_y=Spacer.SMALL.value,
        z_index="999",
        top="0"

    )
