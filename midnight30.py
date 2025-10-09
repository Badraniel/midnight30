from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from thumb_input import ThumbInput
from root_button import RootButton
from colors import colors
from kivy.core.window import Window
from tile import Tile
from kivy.properties import NumericProperty

Window.size = (360, 640)

class TileGrid(GridLayout):
    grid_rows = NumericProperty(10)
    grid_cols = NumericProperty(10)

    def __init__(self, **kwargs):
        super(TileGrid, self).__init__(**kwargs)
        self.rows = self.grid_rows
        self.cols = self.grid_cols
        for i in range(self.grid_rows * self.grid_cols):
            self.add_widget(Tile())

class Screen(FloatLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.start_input()
        self.start_grid()

    def start_input(self):
        self.thumb_input = ThumbInput()
        self.thumb_input.size_hint = (0.44, 0.22)
        self.thumb_input.pos_hint = {"right": 1, "bottom": 0}
        self.add_widget(self.thumb_input)

        # Distância em pixels entre os centros dos botões
        D = 100

        # Conversão para coordenadas relativas
        W = 360  # Largura da janela
        H = 640  # Altura da janela

        Dx = D / W  # Distância horizontal relativa
        Dy = D / H  # Distância vertical relativa

        # Posição do botão A ajustada (mais para baixo e direita)
        offset_x = 60 / W  # 60 pixels da esquerda
        offset_y = 60 / H  # 60 pixels do topo

        # Botão A - canto superior esquerdo ajustado
        self.button_a = RootButton()
        self.button_a.pos_hint = {"center_x": offset_x, "center_y": 1 - offset_y}
        self.button_a.text = "A"
        self.button_a.color = colors["verde_escuro"]
        self.button_a.edge_color = colors["cinza_escuro"]
        self.button_a.text_color = colors["branco"]
        self.add_widget(self.button_a)

        # Botões à direita do A
        self.button_l1 = RootButton()
        self.button_l1.pos_hint = {"center_x": offset_x + Dx, "center_y": 1 - offset_y}
        self.button_l1.text = "L1"
        self.button_l1.color = colors["azul_claro"]
        self.button_l1.edge_color = colors["cinza_escuro"]
        self.button_l1.text_color = colors["branco"]
        self.add_widget(self.button_l1)

        self.button_l2 = RootButton()
        self.button_l2.pos_hint = {"center_x": offset_x + 2 * Dx, "center_y": 1 - offset_y}
        self.button_l2.text = "L2"
        self.button_l2.color = colors["lilas_medio"]
        self.button_l2.edge_color = colors["cinza_escuro"]
        self.button_l2.text_color = colors["branco"]
        self.add_widget(self.button_l2)

        # Botões abaixo do A
        self.button_b1 = RootButton()
        self.button_b1.pos_hint = {"center_x": offset_x, "center_y": 1 - offset_y - Dy}
        self.button_b1.text = "B1"
        self.button_b1.color = colors["laranja_claro"]
        self.button_b1.edge_color = colors["cinza_escuro"]
        self.button_b1.text_color = colors["branco"]
        self.add_widget(self.button_b1)

        self.button_b2 = RootButton()
        self.button_b2.pos_hint = {"center_x": offset_x, "center_y": 1 - offset_y - 2 * Dy}
        self.button_b2.text = "B2"
        self.button_b2.color = colors["vermelho_medio"]
        self.button_b2.edge_color = colors["cinza_escuro"]
        self.button_b2.text_color = colors["branco"]
        self.add_widget(self.button_b2)

    def start_grid(self):
        self.tile_grid = TileGrid()
        self.add_widget(self.tile_grid)

class Midnight30(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    Midnight30().run()