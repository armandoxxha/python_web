import reflex as rx
from proyecto_web.componets.navbar import navbar
from proyecto_web.views.header.headers import headers 
from proyecto_web.links.links import links
from proyecto_web.componets.footer import footer
import proyecto_web.styles.styles as styles
from proyecto_web.views.sponsors.sponsors import sponsors
import proyecto_web.utils as utils
from proyecto_web.api.api import live


class IndexState(rx.State):

    is_live: bool 


    async def check_live(self):
        is_live = await live("armandoxxlml")
    


@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta,
        on_load=IndexState.check_live
)
def index() -> rx.Component:

    return rx.box(
        navbar(),
        utils.lang(),
        rx.center(
            rx.vstack(
                headers(
                    live=IndexState.is_live,
                ),
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
