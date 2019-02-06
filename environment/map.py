from .tile import Tile, GroundTile, PathTile
from units import Enemy

DEFAULT_LAYOUT = """9 8
111101111
111101111
111101111
111101111
111101111
111101111
111101111
111101111"""

class Map():

    def __init__(self, game, layout=DEFAULT_LAYOUT):
        self.game = game
        self.width = -1
        self.height = -1
        self.map = None
        self.layout = layout
        self.load_layout()
        # self.enemy = Enemy(self.game)
        # enemy.spawn()
        self.enemy = None
        # self.enemies = [Enemy()]

    def load_layout(self):
        self.map = []
        layout = self.layout.split('\n')
        self.width, self.height = [int(x) for x in layout.pop(0).split(' ')]
        for i in range(0, self.height):
            map_row = []
            layout_row = layout[i]
            for k, layout_tile in enumerate(list(layout_row)):
                if (layout_tile == "1"):
                    map_row.append(GroundTile(self, k, i))
                else:
                    map_row.append(PathTile(self, k, i))
            self.map.append(map_row)
        

    def render(self):
        for row in self.map:
            for tile in row:
                tile.render()
        if (self.enemy):
            self.enemy.render()







