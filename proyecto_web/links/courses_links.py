import reflex as rx 
from proyecto_web.componets.link_button import link_button
from proyecto_web.componets.title import title
import proyecto_web.contants as const
from proyecto_web.routes import Route

def courses_links() -> rx.Component:

    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Python desde cero",
            "Enlace de canal de youtube de Ernesto",
            const.PYTHON_ERNESTO_URL,
            "/python-brands-solid.svg",
        ),
        link_button(
            "Java desde cero",
            "Enlace de canal de youtube de Ernesto",
            const.JAVA_ERNESTO_URL,
            "/java-brands-solid.svg",
        ),
        link_button(
            "SQL desde cero",
            "Enlace de repositorio de MOUREDEV",
            const.SQL_MOUREDEV_URL,
            "/code-solid.svg",
        ),
        width="100%"

    )