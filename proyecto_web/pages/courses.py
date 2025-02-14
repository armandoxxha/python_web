import reflex as rx
from proyecto_web.componets.navbar import navbar
from proyecto_web.views.header.headers import headers 
from proyecto_web.links.courses_links import courses_links
from proyecto_web.componets.footer import footer
import proyecto_web.styles.styles as styles
from proyecto_web.views.sponsors.sponsors import sponsors
import proyecto_web.utils as utils
from proyecto_web.routes import Route
@rx.page(
        route=Route.COURSES.value,
        title=utils.cursos_title,
        description=utils.cursos_description,
        image=utils.preview,
        meta=utils.cursos_meta
)
def courses() -> rx.Component:

    return rx.box(
        navbar(),
        utils.lang(),
        rx.center(
            rx.vstack(
                headers(details=False),
                courses_links(),
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