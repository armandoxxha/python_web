import reflex as rx
from enum import Enum
from .colores import Color as Color
from .colores import TextColor as TextColor
from .fonts import Font as Font 
from .fonts import FontWeight as FontWeight 
MAX_WIDTH = "560px"

# Sizes 

class Spacer(Enum):
    ZERO="0x !important"
    SMALL="0.5em"
    MEDIUM="0.9em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="4em"

BASE_STYLE  = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display": "block",
        "white_space":"normal",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "text_aling": "start",
        "_hover":{
            "background_color":Color.SECONDARY.value
        }

    }

}
button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size = Spacer.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size = Spacer.MEDIUM.value,
    color=TextColor.BODY.value
)

title_style = dict(
    font_family=Font.TITLE.value,
    size = 'lg',
    width = "100%",
    padding_to = Spacer.DEFAULT.value,
    color=TextColor.HEADER.value
)
navbar_title_style = dict(
    font_family = Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    fon_size = Spacer.LARGE.value
)

STYLESSHEETS = [
        "https://fonts.googleapis.com/css/?family=Poppins:wght@300;500&display=swap",
        "https://fonts.googleapis.com/css/?family=Confortaa:wght@500&display=swap"
]