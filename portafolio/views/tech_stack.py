# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size

# ==============================================
# Componente para mostrar el stack tecnológico
# ==============================================
def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        # ==========================
        # Título de la sección
        # ==========================
        heading("Tecnologías"),
        # ==========================================
        # Contenedor flexible para las tecnologías
        # ==========================================
        rx.flex(
            *[
                # Representación de cada tecnología como una insignia
                rx.badge(
                    # Ícono de la tecnología
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    # Nombre de la tecnología
                    rx.text(technology.name),
                    size="2" # Tamaño de la insignia
                )
                for technology in technologies # Itera sobre la lista de tecnologías
            ],
            wrap="wrap", # Permite que los elementos se ajusten a múltiples líneas si es necesario
            spacing=Size.SMALL.value # Espaciado entre los elementos
        ),
        # ==========================
        # Espaciado general del stack
        # ==========================
        spacing=Size.DEFAULT.value
    )
