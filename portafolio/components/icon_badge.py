# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.styles.styles import EmSize

# ==========================================
# Componente reutilizable para mostrar un ícono dentro de una insignia (badge)
# ==========================================
def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        # ==========================
        # Ícono dentro de la insignia
        # ==========================
        rx.icon(
            icon,
            size=32
        ),
        # ==========================
        # Estilos de la insignia
        # ==========================
        aspect_ratio="1",
        variant="soft"
    )
