import reflex as rx
from portafolio.data import Extra
from portafolio.styles.styles import IMAGE_HEIGHT, Size

def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            href=extra.url,     # ← Mueve href aquí
            is_external=True,   # ← Y también este
            target="_blank"     # ← Esto para abrir en nueva pestaña
        ),
        width="100%",
    )
