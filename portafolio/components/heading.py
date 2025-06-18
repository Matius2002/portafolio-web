# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.styles.styles import Size

# ==========================================
# Componente reutilizable para encabezados
# ==========================================
def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        # ==========================
        # Nivel del encabezado (h1 o h2)
        # ==========================
        as_="h1" if h1 else "h2",
        # ==========================
        # Tamaño visual del encabezado
        # ==========================
        size=Size.BIG.value if h1 else Size.MEDIUM.value
    )
