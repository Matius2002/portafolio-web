# ==========================
# Importaciones necesarias
# ==========================
from enum import Enum
import reflex as rx

# ==========================
# Constantes globales de estilo
# ==========================
MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

# ==========================
# Enumeración para tamaños relativos (em)
# ==========================
class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"

# ==========================
# Enumeración para espaciados (basado en escala de 4px)
# ==========================
class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px

# ==========================
# Hojas de estilo externas
# ==========================
STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

# ==========================
# Estilos base personalizados globales
# ==========================
BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}
