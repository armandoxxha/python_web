import reflex as rx

import proyecto_web.styles.styles as styles 
from proyecto_web.styles.styles import Spacer as Sparcer 


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Sparcer.VERY_BIG.value,
            width="auto",
            src=imagen,
            alt=alt
        ),
        href=url,
        is_external=True
    )