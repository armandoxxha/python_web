import reflex as rx 
from proyecto_web.componets.navbar import navbar
from proyecto_web.views.header.headers import headers 
from proyecto_web.links.links import links
from proyecto_web.componets.footer import footer
import proyecto_web.styles.styles as styles
from proyecto_web.views.sponsors.sponsors import sponsors
class State(rx.State):
    pass

def index() -> rx.Component:

    return rx.box(
        navbar(),
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

app = rx.App(
    stylesheets=styles.STYLESSHEETS,
    style=styles.BASE_STYLE,
   
)
app.add_page(
    index,
    title="Armandoxx | Te enseño programación y desarrollo de software",
    description="Hola, mi nombre es Armando Hidalgo. Soy docente de informática",
    image="avatar1.jpg"
    )
app._compile()