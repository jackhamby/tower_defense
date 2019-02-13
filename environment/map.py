from .tile import Tile, GroundTile, PathTile
from units import Enemy
import math
import pygame

DEFAULT_LAYOUT = """9 8
111101111
111101111
111101111
111101111
111101111
111101111
111101111
111101111"""

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Map():

    def __init__(self, game, layout=DEFAULT_LAYOUT):
        self.game = game
        self.width = -1
        self.height = -1
        self.map = None
        self.layout = layout
        self.load_layout()
        self.current_round = None
        self.towers = []
        self.selected_tower = None


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
        

    def get_tile(self, x, y):
        tile = None
        tile_width = math.floor(SCREEN_WIDTH / self.width)
        tile_height = math.floor(SCREEN_HEIGHT / self.height)
        x_index = math.floor(x / tile_width)
        y_index = math.floor( y / tile_height)
        if (x_index >= 0 and x_index < self.width and
            y_index >= 0 and y_index < self.height):
            tile = self.map[y_index][x_index]
        return tile


    def render(self):
        for row in self.map:
            for tile in row:
                tile.render()
        for tower in self.towers:
            tower.render()
        if (self.selected_tower):
            pygame.draw.circle(self.game.screen, (111, 111, 111), (self.selected_tower.x + math.floor(self.selected_tower.width/2), self.selected_tower.y + math.floor(self.selected_tower.height/2)), self.selected_tower.range, 2)
        if (self.current_round):
            for enemy in self.current_round.enemies:
                enemy.render()








