import reflex as rx 
import datetime
from proyecto_web.styles.styles import Spacer as Spacer
from proyecto_web.styles.colores import TextColor as TextColor
import proyecto_web.contants as const

def footer() -> rx.Component:

    return rx.vstack(
        rx.image(
            src="/logo.png",
            width=Spacer.VERY_BIG.value,
            height=Spacer.VERY_BIG.value,
            alt="Logotipo de armando"
            
        ),
        rx.link(
            f"© 2020-{datetime.date.today().year} ARMANDOXX BY ARMANDO HIDALGO",
            href=const.TWITCH_URL,
            is_external=True,
            font_size=Spacer.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/github-brands-solid.svg",
                      width=Spacer.LARGE.value,
                      height=Spacer.LARGE.value
                ),
                rx.text(
                    "V3.BUILDING SOFTWARE WITH ♥ FROM GALACIA TO THE WORLD",
                    font_size=Spacer.MEDIUM.value,
                    margin_top=Spacer.ZERO.value
                )
            ),
            href=const.CODIGO_PAGINA_WEB_GITHUB,
            is_external=True
        )
        ,
        align="center",
        margin_botton=Spacer.BIG.value,
        padding_x=Spacer.BIG.value,
        padding_botton=Spacer.BIG.value,
        color = TextColor.FOOTER.value
    )