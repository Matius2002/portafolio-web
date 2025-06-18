# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size

# ==========================================
# Componente principal del encabezado (header)
# ==========================================
def header(data: Data) -> rx.Component:
    return rx.hstack(
        # ======================
        # Imagen de avatar
        # ======================
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
        ),
        # ======================
        # Información del usuario (nombre, skill, ubicación, redes)
        # ======================
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            # Ubicación con ícono
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            # Redes sociales u otros medios
            media(data.media),
            # Espaciado interno entre los elementos del bloque vertical
            spacing=Size.SMALL.value,
        ),
        # Espaciado entre el avatar y el bloque de información
        spacing=Size.DEFAULT.value,
    )
