import reflex as rx 
from proyecto_web.componets.link_button import link_button
from proyecto_web.componets.title import title
import proyecto_web.contants as const

def links() -> rx.Component:

    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de Lunes a Viernes",
            const.TWITCH_URL,
            "twitch-brands-solid.svg"
        ),
        link_button(
            "YouTube",
            "Mi canal de Youtube",
            const.YOUTUBE_URL,
            "youtube-brands-solid.svg"
        ),
        link_button(
            "GITHUB Python Inicial Octavo",
            "Enlace a repositorio de github de octavo",
            const.GIT_HUBPYTHONINICIAL_URL,
            "github-brands-solid.svg"
        ),
        link_button(
            "GITHUB Python avanzado Noveno",
            "Enlace a repositorio de github de noveno",
            const.GIT_HUBPYTHONINICIAL_URL,
            "github-brands-solid.svg"
        ),
        title("Recursos y más"),
        link_button(
            "Enlace a Codedex",
            "Aquí encontraras el sitio web de codedex.com ",
            const.CODEDEX_URL,
            "laptop-solid.svg"
        ),
        link_button(
            "Libros recomendados",
            "Mi listado de libros sobre programacion, ciencia y tecnologia",
            "https://youtube.com/@mouredev",
            "book-solid.svg"
        ),
        link_button(
            "Recursos 7 del 2024",
            "Materiales vistos en clases en septimo 2024",
            const.DRIVE7_2024_URL,
            "google-drive-brands-solid.svg"
        ),
        link_button(
            "Recursos 8 del 2024",
            "Materiales vistos en clases en octavo 2024",
            const.DRIVE8_2024_URL,
            "google-drive-brands-solid.svg"

        ),
        link_button(
            "Python Download",
            "Enlace para descargar la suite de python",
            const.PYTHON_URL,
            "python-brands-solid.svg"
        ),
        link_button(
            "Visual Studio Code",
            "Enlace para descargar la suite de visual studio",
            const.VISUAL_STUDIO_URL,
            "microsoft-brands-solid.svg"
        ),
        title("Contactos"),
        link_button(
            "My public inbox",
            "Respuesta rapida y con preferencia",
            const.MYPUBLICINBOX_URL,
            "envelope-solid.svg"
        ),
        link_button(
            "Email",
            const.EMAIL,
            f"mailto:{const.EMAIL}",
            "envelope-solid.svg"
        ),
        width="100%"

    )