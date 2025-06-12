import reflex as rx
from portafolio.components.heading import heading

def about(description: list[str]) -> rx.Component:
    
    return rx.vstack(
        heading("Sobre mí"),
        *[rx.text(paragraph) for paragraph in description] #Separación de parrafos en Sobre mí
    )
    
