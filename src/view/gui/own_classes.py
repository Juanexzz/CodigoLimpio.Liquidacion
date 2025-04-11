from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle


class BackgroundLabel(Label):
    def __init__(self, background_color = (0, 0, 0, 0), **kwargs):
        super().__init__(**kwargs)
        self.background_color = background_color
        with self.canvas.before:
            self.bg_color = Color(*self.background_color)
            self.bg_rect = Rectangle(pos = self.pos, size = self.size)
        self.bind(pos = self._update_bg, size = self._update_bg)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
