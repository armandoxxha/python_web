import reflex as rx 
import proyecto_web.styles.styles as styles
from proyecto_web.styles.styles import Spacer

def link_button(title : str, body: str, url: str, image:str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Spacer.BIG.value,
                    height=styles.Spacer.BIG.value,
                    margin=Spacer.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="4",
                    align="start",
                    padding_y=Spacer.SMALL.value,
                    padding_right=Spacer.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )

