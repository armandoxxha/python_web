import reflex as rx
import proyecto_web.styles.styles as styles
from proyecto_web.componets.info_text import info_text
from proyecto_web.componets.lin_icon import link_icon
from proyecto_web.styles.styles import TextColor as TextColor
from proyecto_web.styles.styles import Color as Color
from proyecto_web.styles.styles import Spacer as Sparcer
import proyecto_web.contants as const
from proyecto_web.componets.title import title
from proyecto_web.componets.link_sponsors import link_sponsor

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "/LT.png",
                const.LICEO_URL,
                "LiceoTucurrique"
            ),
            link_sponsor(
                "/MEP.png",
                const.MEP_URL,
                "MEP"
            ),
            spacing='9',
            columns=[1,2]
        ),
        width="100%",
        align='start',
        spacing='9'


    )