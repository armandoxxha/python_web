import reflex as rx 
from proyecto_web.componets.navbar import navbar
from proyecto_web.views.header.headers import headers 
from proyecto_web.links.links import links
from proyecto_web.componets.footer import footer
import proyecto_web.styles.styles as styles
from proyecto_web.views.sponsors.sponsors import sponsors
from proyecto_web.pages.index import index
from proyecto_web.pages.courses import courses
from proyecto_web.api.api import repo, live

app = rx.App(
    stylesheets=styles.STYLESSHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletamanager.com/gtag/js?id=GTM-T9CRRMN5"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'GTM-T9CRRMN5')
"""
        ),
    ],
   
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)