from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.graphics import Color, Line, Rectangle


class ThumbInput(BoxLayout):
    status_text = StringProperty("Pronto para ação")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

            Color(1, 0.8, 0, 1)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(pos=self._update_canvas, size=self._update_canvas)

    def _update_canvas(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.status_text = "Toque iniciado"
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.status_text = f"Movendo: {touch.spos}"
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.status_text = "Toque finalizado"
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)