from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, DictProperty, ObjectProperty
from kivy.metrics import dp
import colors

class Obj(Widget):
    # Propriedade numérica
    hp = NumericProperty(25)

    properties = DictProperty({})
    active_effects = DictProperty({})
    relations = DictProperty({})

    #oi