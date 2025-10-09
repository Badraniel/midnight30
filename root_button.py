from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder
from colors import colors

Builder.load_file('root_button.kv')

class RootButton(BoxLayout):
    text = StringProperty('')
    color = ListProperty(colors['lilas_medio'])
    edge_color = ListProperty(colors['cinza_escuro'])
    text_color = ListProperty(colors['branco'])

    def on_touch_down(self, touch):
        # Verifica se o toque ocorreu dentro deste widget
        if self.collide_point(*touch.pos):
            # Armazena a cor ORIGINAL da borda no touch.ud
            touch.ud['original_edge_color'] = self.edge_color
            # Muda a borda para dourado
            self.edge_color = colors['dourado_claro']
            # "Agarra" o toque para receber os eventos subsequentes
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        # Verifica se este widget está "segurando" o toque
        if touch.grab_current is self:
            # Restaura a cor ORIGINAL que estava salva no touch.ud
            self.edge_color = touch.ud.get('original_edge_color', self.edge_color)
            # Para de "agarrar" o toque
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)