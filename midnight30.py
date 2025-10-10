from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from thumb_input import ThumbInput
from root_button import RootButton
from colors import colors
from kivy.core.window import Window
from tile import Tile
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder # Importar Builder

# Carregar o arquivo KV principal explicitamente
Builder.load_file("main_screen.kv")

Window.size = (360, 640)

print("oioi")

# Removendo a classe TileGrid, pois agora usamos CustomTileGrid
# class TileGrid(GridLayout):
#     grid_rows = NumericProperty(10)
#     grid_cols = NumericProperty(10)

#     def __init__(self, **kwargs):
#         super(TileGrid, self).__init__(**kwargs)
#         self.rows = self.grid_rows
#         self.cols = self.grid_cols
#         for i in range(self.grid_rows * self.grid_cols):
#             self.add_widget(Tile())

class CustomTileGrid(FloatLayout):
    # Propriedades do grid
    grid_rows = NumericProperty(10)
    grid_cols = NumericProperty(10)
    tile_size_dp = NumericProperty(28) # Tamanho de cada tile em dp
    spacing_dp = NumericProperty(1) # Espaçamento entre tiles em dp

    # Ponto de início do grid (canto inferior esquerdo do grid)
    # Estas propriedades serão definidas pelo pai (Screen) para posicionar o grid
    # Os tiles internos serão posicionados relativos a este ponto.
    grid_origin_x = NumericProperty(0)
    grid_origin_y = NumericProperty(0)
    grid_origin = ReferenceListProperty(grid_origin_x, grid_origin_y)

    def __init__(self, **kwargs):
        super(CustomTileGrid, self).__init__(**kwargs)
        # Vincula a atualização do layout a mudanças de tamanho ou posição do próprio grid
        # ou quando as propriedades do grid (linhas, colunas, tamanho do tile, espaçamento) mudam.
        self.bind(pos=self.update_grid_layout, size=self.update_grid_layout,
                  grid_rows=self.update_grid_layout, grid_cols=self.update_grid_layout,
                  tile_size_dp=self.update_grid_layout, spacing_dp=self.update_grid_layout)
        # Agenda a primeira atualização para garantir que o tamanho da janela esteja disponível
        Clock.schedule_once(self.update_grid_layout, 0)

    def update_grid_layout(self, *args):
        # Limpa todos os tiles existentes antes de redesenhar
        self.clear_widgets()

        # --- Definições de Dimensões --- #
        # Converte o tamanho do tile e espaçamento de dp para pixels reais
        current_tile_width = dp(self.tile_size_dp)
        current_tile_height = dp(self.tile_size_dp)
        current_spacing = dp(self.spacing_dp)

        # Calcula a largura e altura total que o grid ocupará
        # (Número de colunas * largura do tile) + (Número de espaços horizontais * espaçamento)
        total_grid_width = (self.grid_cols * current_tile_width) + ((self.grid_cols - 1) * current_spacing)
        # (Número de linhas * altura do tile) + (Número de espaços verticais * espaçamento)
        total_grid_height = (self.grid_rows * current_tile_height) + ((self.grid_rows - 1) * current_spacing)

        # Ajusta o tamanho do CustomTileGrid para o tamanho calculado
        # Isso é importante para que o pai (Screen) possa posicionar este widget corretamente
        self.size = (total_grid_width, total_grid_height)

        # --- Geração e Posicionamento dos Tiles --- #
        for row_index in range(self.grid_rows):
            for col_index in range(self.grid_cols):
                tile = Tile()
                # Define que o tamanho do tile é fixo, não relativo ao pai
                tile.size_hint = (None, None) # Tamanho fixo, não relativo ao pai
                tile.size = (current_tile_width, current_tile_height)

                # --- Matemática de Posicionamento Legível --- #
                # Calcula a posição X do canto inferior esquerdo do tile
                # Começa do \'0\' do CustomTileGrid (que é o seu próprio canto inferior esquerdo)
                # Adiciona o deslocamento horizontal: (índice da coluna * (largura do tile + espaçamento))
                calculated_x_relative_to_grid = col_index * (current_tile_width + current_spacing)

                # Calcula a posição Y do canto inferior esquerdo do tile
                # O Kivy desenha de baixo para cima. Para que a \'linha 0\' seja a do topo do grid,
                # precisamos inverter a contagem das linhas: (total de linhas - 1 - índice da linha atual).
                # Adiciona o deslocamento vertical: (índice da linha invertido * (altura do tile + espaçamento))
                calculated_y_relative_to_grid = (self.grid_rows - 1 - row_index) * (current_tile_height + current_spacing)

                # Define a posição final do tile, relativa ao canto inferior esquerdo do CustomTileGrid
                tile.pos = (self.x + calculated_x_relative_to_grid, self.y + calculated_y_relative_to_grid)

                self.add_widget(tile)
                # print(f"[DEBUG] Tile[{row_index},{col_index}] pos=({tile.x:.2f}, {tile.y:.2f}) size={tile.size}")

        print(f"[DEBUG] CustomTileGrid final size={self.size}, pos={self.pos}")

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
        self.custom_tile_grid = CustomTileGrid()
        self.custom_tile_grid.size_hint = (None, None) # O tamanho será definido internamente pelo CustomTileGrid

        # Força o cálculo do tamanho do grid antes de posicioná-lo
        # Isso garante que self.custom_tile_grid.width e .height tenham valores corretos
        self.custom_tile_grid.update_grid_layout() 

        # --- Matemática de Posicionamento do Grid na Tela --- #
        # Define as margens desejadas do canto superior direito da janela
        margin_right = dp(10) # 10 pixels da borda direita
        margin_top = dp(10)   # 10 pixels da borda superior

        # Calcula a posição X do canto inferior esquerdo do CustomTileGrid
        # Largura da janela - largura total do grid - margem direita
        calculated_grid_x = Window.width - self.custom_tile_grid.width - margin_right

        # Calcula a posição Y do canto inferior esquerdo do CustomTileGrid
        # Altura da janela - altura total do grid - margem superior
        calculated_grid_y = Window.height - self.custom_tile_grid.height - margin_top

        # Aplica a posição calculada ao CustomTileGrid
        self.custom_tile_grid.pos = (calculated_grid_x, calculated_grid_y)

        # Adiciona o CustomTileGrid à tela principal
        self.add_widget(self.custom_tile_grid)

class Midnight30(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    Midnight30().run()