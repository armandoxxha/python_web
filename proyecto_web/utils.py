import reflex as rx

# Comun
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://armando-web.vercel.app/avatar1.jpg"

_meta = [
    {"name": "og:type", "content":"website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]

# Index 

index_title = "Armandoxx | Te enseño programación y desarrollo de software"
index_description = "Hola, mi nombre es Armando Hidalgo. Soy docente de informática"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos

cursos_title = "Armandoxx | Cursos gratis"
cursos_description = "Este es un listado de cursos gratis para aprender sobre informatica. Python, redes"
cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description},
]
cursos_meta.extend(_meta)