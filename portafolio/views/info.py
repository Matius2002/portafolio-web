# -----------------------------------------
# IMPORTACIONES NECESARIAS
# -----------------------------------------
import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size

# -----------------------------------------
# FUNCIÓN info
# -----------------------------------------
def info(title: str, info: list[Info]) -> rx.Component:
    """
    Renderiza una sección del portafolio como 'Experiencia', 'Proyectos' o 'Formación'.

    Parámetros:
    - title (str): Título de la sección.
    - info (list[Info]): Lista de elementos de tipo Info (experiencia, proyectos, etc.).

    Retorna:
    - rx.Component: Un componente vertical que contiene el título y los detalles de la sección.
    """
    return rx.vstack(
        heading(title), # Encabezado de la sección
        rx.vstack(
            *[
                info_detail(item) # Renderiza cada ítem usando el componente info_detail
                for item in info
            ],
            spacing=Size.DEFAULT.value, # Espaciado entre ítems
            width="100%" # Ancho completo
        ),
        spacing=Size.DEFAULT.value, # Espaciado entre título y contenido
        width="100%" # Ancho completo del bloque principal
    )
