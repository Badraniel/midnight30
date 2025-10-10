from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.lang import Builder
import colors

Builder.load_file("tile.kv")


class Tile(Widget):
    # Propriedades específicas do Tile
    bound_object = [None]
    bound_mob = [None]

    # Properties for animation - defined here for access in KV file
    bg_alpha = NumericProperty(0.1)  # Initial alpha for background
    border_alpha = NumericProperty(0.1)  # Initial alpha for border

    # Usar ListProperty para cores para que o KV possa acessá-las diretamente como listas
    bg_color = ListProperty(colors.colors["branco"])
    border_color = ListProperty(colors.colors["cinza_medio"])

    def __init__(self, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(25), dp(25))
        self.spawn()

    def spawn(self):
        # Create animations for the alpha properties
        # Animate both background and border alpha to 1 over 2 seconds
        anim_bg = Animation(bg_alpha=1, border_alpha=1, duration=.5)
        # Start both animations
        anim_bg.start(self)

    def update_canvas(self):
        self.canvas.ask_update()