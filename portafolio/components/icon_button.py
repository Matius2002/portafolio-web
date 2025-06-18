# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx

# ==========================================
# Componente de botón con ícono y enlace externo
# ==========================================
def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            # ==========================
            # Contenido del botón
            # ==========================
            rx.icon(icon),
            text,
            # ==========================
            # Estilo visual del botón
            # ==========================
            variant="solid" if solid else "surface"
        ),
        # ==========================
        # Propiedades del enlace
        # ==========================
        href=url,
        is_external=True
    )
