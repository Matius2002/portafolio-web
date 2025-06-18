# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.data import Extra
from portafolio.styles.styles import IMAGE_HEIGHT, Size

# ========================================
# Componente de tarjeta para un elemento Extra
# ========================================
def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            # ======================
            # Imagen principal del recurso
            # ======================
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            # ======================
            # Título del recurso
            # ======================
            rx.text.strong(extra.title),
            # ======================
            # Descripción del recurso
            # ======================
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            # ======================
            # Configuración del enlace
            # ======================  
            href=extra.url,     # ← Mueve href aquí
            is_external=True,   # ← Y también este
            target="_blank"     # ← Esto para abrir en nueva pestaña
        ),
        # ======================
        # Ancho total para adaptabilidad
        # ======================
        width="100%",
    )
