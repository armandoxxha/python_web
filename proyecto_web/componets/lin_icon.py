import reflex as rx
import proyecto_web.styles.styles as styles 
from proyecto_web.styles.styles import Spacer as Sparcer

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Sparcer.MEDIUM.value,
            alt=alt
        ),
        href=url,
        is_external=True 
    )