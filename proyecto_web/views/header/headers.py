import reflex as rx 
import proyecto_web.styles.styles as styles
from proyecto_web.componets.info_text import info_text
from proyecto_web.componets.lin_icon import link_icon
from proyecto_web.styles.styles import TextColor as TextColor
from proyecto_web.styles.styles import Color as Color
from proyecto_web.styles.styles import Spacer as Sparcer
import proyecto_web.contants as const
def headers(details = True, live = False) -> rx.Component:

    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Armando Hidalgo A",
                src="/avatar1.jpg",
                fallback="AH", size='7',
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                radius="full"

            ),
            rx.vstack(
                rx.heading(
                    "ARMANDO HIDALGO A",
                    size='6',
                    color = TextColor.HEADER.value
                ),
                rx.text(
                    "@armandoxx",
                    margin_top = Sparcer.ZERO.value,
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "/twitch-brands-solid.svg",
                        const.TWITCH_URL,
                        "Twitch"
                    ),
                    link_icon(
                        "/youtube-brands-solid.svg",
                        const.YOUTUBE_URL,
                        "Youtube"
                    ),
                    link_icon(
                        "/github-brands-solid.svg",
                        const.GIT_HUB_URL,
                        "github"
                    )
                ),

                width="100%"
            ),
            align="start",
            spacing='6'
        ),
        rx.cond(
            details,
            rx.box(        
                rx.flex(
                    info_text("+9 ", "años de experiencia en docencia"),
                    rx.spacer(),
                    info_text("+2 ", "años de experiencia en Ciberseguridad"),
                    rx.spacer(),
                    info_text("+4 ", "años de experiencia Networking"),
                    width="100%"

                ),
                rx.text(
                    "HOLA MI NOMBRE ES ARMANDO HIDALGO",
                    color = TextColor.HEADER.value, 
                    align="center"
                ), 
                rx.text(
                    f"""Soy un entusiasta de la programación de software. Actualmente
                    trabajo como docente de informática. La siguiente web recoge diferentes
                    links de información correspondiente a mi área, espero te sirva""",
                    width="100%",
                    align="center",
                    font_size=Sparcer.DEFAULT.value,
                    color = TextColor.BODY.value
                ),
                width="100%"
                
            )
        ),
        align="center",
        spacing='9',
        align_items="start"
    )