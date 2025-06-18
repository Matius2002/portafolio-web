# ==========================
# Importaciones necesarias
# ==========================
import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

# ==========================================================
# Componente visual que representa los detalles de un ítem Info
# (como experiencia, proyecto o certificación)
# ==========================================================
def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        # =====================================
        # Columna principal con el contenido textual
        # =====================================
        rx.hstack(
            # Ícono decorativo principal
            icon_badge(info.icon),
            # Bloque de texto con los detalles
            rx.vstack(
                # Título destacado
                rx.text.strong(info.title),
                # Subtítulo o nombre de entidad/empresa
                rx.text(info.subtitle),
                # Descripción general
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray",
                    text_align="justify" #Justificación del texto de Experiencia.
                ),
                # =====================================
                # Tecnologías asociadas (badges grises)
                # =====================================
                rx.flex(
    *[
        rx.badge(
            rx.box(class_name=technology.icon),
            technology.name,
            color_scheme="gray"
        )
        for technology in info.technologies
    ],
    wrap="wrap",
    spacing=Size.SMALL.value
) if info.technologies else rx.fragment()
,
                # =====================================
                # Botones de enlace (URL y GitHub)
                # =====================================
                rx.hstack(
                    # Enlace principal si existe
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    # Enlace a GitHub si existe
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                # Espaciado interno del bloque
                spacing=Size.SMALL.value,
                width="100%"
            ),
            # Espaciado entre el ícono y el bloque de texto
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        # =====================================
        # Imagen ilustrativa si está disponible
        # =====================================
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height="200px",
                width="350px",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover",
                box_shadow="lg"
            )
        ),
        # =====================================
        # Columna lateral con fecha y certificado
        # =====================================
        rx.vstack(
            # Fecha (si está disponible)
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            # Certificado descargable (si existe)
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        # =====================================
        # Estilos del contenedor general
        # =====================================
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
