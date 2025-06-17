# -----------------------------------------
# IMPORTACIÓN DE MÓDULOS Y COMPONENTES
# -----------------------------------------
import reflex as rx # Framework para crear aplicaciones web en Python (anteriormente Pynecone)
from portafolio import data # Carga los datos estructurados desde data.py
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

# -----------------------------------------
# OBTENCIÓN DE DATOS
# -----------------------------------------
DATA = data.data # Objeto principal con toda la información del portafolio

# -----------------------------------------
# DEFINICIÓN DE LA PÁGINA PRINCIPAL
# -----------------------------------------
def index() -> rx.Component:
    """
    Página principal de la aplicación.
    Compuesta por diferentes secciones del portafolio como:
    encabezado, acerca de mí, pila tecnológica, experiencia,
    proyectos, formación, contenido extra y pie de página.
    """
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formación", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )

# -----------------------------------------
# CONFIGURACIÓN DE LA APLICACIÓN
# -----------------------------------------
app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="grass",
        radius="full"
    )
)

# -----------------------------------------
# CONFIGURACIÓN DE LA PÁGINA INDEX
# -----------------------------------------
title = DATA.title
description = DATA.description
image = DATA.image

# Registro de la página en la aplicación
app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
