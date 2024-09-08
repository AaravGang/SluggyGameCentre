import pygame
from pygame import freetype

pygame.font.init()
freetype.init()


class Font(pygame.font.Font):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, text, antalias, color, background=None, size=0):
        return super().render(text, antalias, color, background,)


class FreetypeFont(freetype.Font):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(
        self, text, antalias, color, background=None, size=0, bold=False, italic=False
    ):
        bold = freetype.STYLE_STRONG if bold else 0
        italic = freetype.STYLE_OBLIQUE if italic else 0
        return super().render(text, color, background, size=size, style=bold | italic)[
            0
        ]

    def size(self, text, *args, **kwargs):
        return super().get_rect(text, *args, **kwargs)
