# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size

# ==========================================================
# Componente que muestra la información de contacto y enlaces sociales
# ==========================================================
def media(data: Media) -> rx.Component:
    return rx.flex(
        # =====================================
        # Botón de correo electrónico
        # =====================================
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True
        ),
        # =====================================
        # Bloque de botones sociales y CV
        # =====================================
        rx.hstack(
            # Botón para descargar o ver el CV
            icon_button(
                "file-text",
                data.cv
            ),
            # Enlace al perfil de GitHub
            icon_button(
                "github",
                data.github
            ),
            # Enlace al perfil de LinkedIn
            icon_button(
                "linkedin",
                data.likedin
            ),
            spacing=Size.SMALL.value
        ),
        # =====================================
        # Estilos generales del contenedor
        # =====================================
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )
