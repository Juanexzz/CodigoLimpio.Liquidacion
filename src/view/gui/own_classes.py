class BackgroundLabel(Label):
    def __init__(self, background_color = (0,0,0,0), **kwargs):
        super().__init__(**kwargs)
        self.background_color = background_color
        with self.canvas.before:
            self.bg_color = Color(*self.background_color)