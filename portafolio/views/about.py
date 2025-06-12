import reflex as rx
from portafolio.components.heading import heading

def about(description: list[str]) -> rx.Component:
    
    return rx.vstack(
        heading("Sobre mí"),
        *[
            rx.text(
                paragraph,
                text_align="justify",         # Justifica el texto
                margin_bottom="1em",          # Espacio entre párrafos
                font_size="0.9em",            # Opcional: tamaño de fuente más cómodo
                width="100%",                 # Opcional: adapta al contenedor
                max_width="800px",            # Opcional: limita el ancho para mejor lectura
            )
            for paragraph in description
        ],
        align_items="start"  # Alinea todo a la izquierda
    )
    
