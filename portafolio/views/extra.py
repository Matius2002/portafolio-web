# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size

# ==========================================
# Componente principal para la vista "Extra"
# ==========================================
def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        # ==========================
        # Vista para dispositivos móviles
        # ==========================
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(extra) # Renderiza cada tarjeta en una columna vertical
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value # Espaciado entre tarjetas
            ),
            width="100%" # Ocupa todo el ancho disponible
        ),
        # ==============================
        # Vista para tabletas y escritorios
        # ==============================
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(extra) # Renderiza cada tarjeta en una cuadrícula
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value, # Espaciado entre tarjetas
                columns="3" # Tres columnas en vista de escritorio
            ),
            width="100%" # Ocupa todo el ancho disponible
        ),
        # ==============================
        # Espaciado general del contenedor
        # ==============================
        spacing=Size.DEFAULT.value,
        width="100%"
    )
