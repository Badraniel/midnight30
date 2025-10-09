from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
import colors


class Tile(Widget):
    # Propriedades específicas do Tile
    bound_object = [None]
    bound_mob = [None]
    #properties = {}
    #active_effects = {}
    #relations = {}
#
    ## Properties for animation - defined here for access in KV file
    bg_alpha = NumericProperty(0.1)  # Initial alpha for background
    border_alpha = NumericProperty(0.1)  # Initial alpha for border
    bg_color = StringProperty('branco')
    border_color = StringProperty('cinza-medio')
    def __init__(self, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(25), dp(25))
        self.spawn()

    @property
    def bg_color(self):
        return colors[self.bg_color]

    @property
    def border_color(self):
        return colors[self.border_color]

    def spawn(self):
        # Create animations for the alpha properties
        # Animate both background and border alpha to 1 over 2 seconds
        anim_bg = Animation(bg_alpha=1,border_alpha=1, duration=2)
        # Start both animations
        anim_bg.start(self)

    def update_canvas(self):
        self.canvas.ask_update()