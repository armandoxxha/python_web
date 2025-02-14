import reflex as rx

config = rx.Config(
    app_name="proyecto_web",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://armando-web.vercel.app/"
    ]
)