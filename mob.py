from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, DictProperty, ObjectProperty
from kivy.metrics import dp
import colors

class Mob(Widget):
    # Propriedades numéricas
    hp = NumericProperty(100)
    mana = NumericProperty(100)


    properties = DictProperty({})
    active_effects = DictProperty({})
    relations = DictProperty({})