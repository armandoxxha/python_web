import reflex as rx
from proyecto_web.componets.navbar import navbar
from proyecto_web.views.header.headers import headers 
from proyecto_web.links.links import links
from proyecto_web.componets.footer import footer
import proyecto_web.styles.styles as styles
from proyecto_web.views.sponsors.sponsors import sponsors
import proyecto_web.utils as utils
@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta
)
def index() -> rx.Component:

    return rx.box(
        navbar(),
        utils.lang(),
        rx.center(
            rx.vstack(
                headers(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Spacer.BIG.value,
                padding=styles.Spacer.BIG.value

            )
        ),
        
        rx.center(
            footer()
        )
    )
