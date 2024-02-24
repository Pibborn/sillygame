from rich.style import Style
import os

class Const:
    STYLE_TITLE = Style(color="red", blink=True, bold=True)
    PETS_PATH = 'resources' + os.sep + 'pets.json'


