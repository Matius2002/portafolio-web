# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size

# ==========================================
# Componente principal del pie de página (footer)
# ==========================================
def footer(data: Media) -> rx.Component:
    return rx.vstack(
        # Texto del nombre (puede representar el autor o marca)
        rx.text("Nombre"),
        # Sección de medios (redes sociales, enlaces, etc.)
        media(data),
        # Espaciado vertical entre elementos del footer
        spacing=Size.SMALL.value
    )
