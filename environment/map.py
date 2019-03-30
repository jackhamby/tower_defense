from .tile import Tile, GroundTile, PathTile
from interface import TowerSelect, TowerDetail
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .round import Round
# from enemies import K
import math
import pygame
import environment

# DEFAULT_LAYOUT = """9 8
# 1111e1111
# 111101111
# 111101111
# 111101111
# 111101111
# 111101111
# 111101111
# 1111s1111"""

# DEFAULT_LAYOUT = """9 8
# 111111111
# 111111111
# e00001111
# 111101111
# 111101111
# 111101111
# 111101111
# 1111s1111"""

# DEFAULT_LAYOUT = """9 8
# 11e111111
# 110111111
# 110000011
# 111111011
# 111111011
# 111100011
# 111101111
# 1111s1111"""


DEFAULT_LAYOUT = """9 8
111111111
e00000011
111111011
111111011
111111011
111100011
111101111
1111s1111"""

# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 800


class Map():

    def __init__(self, layout=DEFAULT_LAYOUT):
        self.screen = environment.Game.screen
        self.width = -1
        self.height = -1
        self.starting_tile = None
        self.ending_tile = None
        self.selected_tower = None

        # Towers
        self.towers = []

        # Interface
        # self.interface_components = [TowerDetail(self), TowerSelect(self)]
        self.tower_detail = TowerDetail(self)
        self.tower_select = TowerSelect(self)

        # Enemies 
        self.enemies = []

        # Tiles
        self.tiles = []

        # Set first round
        self.round = Round(self, 1)

        # Initialize board with tiles using layout template
        self.load_layout(layout)

    
    def load_layout(self, layout):
        self.tiles = []
        layout = layout.split('\n')
        self.width, self.height = [int(x) for x in layout.pop(0).split(' ')]
        tile_width = math.floor(SCREEN_WIDTH / self.width)
        tile_height = math.floor(SCREEN_HEIGHT / self.height)
        for i in range(0, self.height):
            map_row = []
            layout_row = layout[i]
            for k, layout_tile in enumerate(list(layout_row)):
                if (layout_tile == "1"):
                    map_row.append(GroundTile(tile_width, tile_height,  k, i)) # Ground tile
                elif(layout_tile == "0"):
                    map_row.append(PathTile(tile_width, tile_height, k, i)) # Path tile
                elif(layout_tile == "s"):
                    self.starting_tile = PathTile(tile_width, tile_height, k, i, is_start=True)
                    map_row.append(self.starting_tile) # Starting tile
                elif(layout_tile == "e"):
                    self.ending_tile = PathTile(tile_width, tile_height, k, i, is_end=True)
                    map_row.append(self.ending_tile) # Ending tile        
            self.tiles.append(map_row)

        # print('loaded layout')
        # print(self.starting_tile)



    def get_tile(self, x, y):
        tile = None
        tile_width = math.floor(SCREEN_WIDTH / self.width)
        tile_height = math.floor(SCREEN_HEIGHT / self.height)
        x_index = math.ceil(x / tile_width) - 1
        y_index = math.ceil( y / tile_height) - 1
        if (x_index >= 0 and x_index <= self.width and
            y_index >= 0 and y_index <= self.height):
            tile = self.tiles[y_index][x_index]
        return tile


    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()
        for tower in self.towers:
            tower.render()
        for enemy in self.enemies:
            enemy.render()

        self.tower_detail.render()
        self.tower_select.render()

        if (self.round.is_started and len(self.round.enemy_pool) == 0 and len(self.enemies) == 0):
            self.round.stop()

        if (self.selected_tower):
            pygame.draw.circle(self.screen, (111, 111, 111), (self.selected_tower.x + math.floor(self.selected_tower.width/2), self.selected_tower.y + math.floor(self.selected_tower.height/2)), self.selected_tower.range, 2)

        for tower in self.towers:
            tower.try_attack()

    def handle_mouse_down(self, x, y):
        # for component in self.interface_components:
        #     component.handle_mouse_down(x, y)
        self.tower_detail.handle_mouse_down(x, y)
        self.tower_select.handle_mouse_down(x, y)
        for tower in self.towers:
            tower.handle_mouse_down(x, y)

    def handle_mouse_up(self, x, y):
        # for component in self.interface_components:
        #     component.handle_mouse_up(x, y)
        self.tower_detail.handle_mouse_up(x, y)
        self.tower_select.handle_mouse_up(x, y)
        for tower in self.towers:
            tower.handle_mouse_up(x, y)

    def handle_mouse_motion(self, x, y):
        for tower in self.towers:
            tower.handle_mouse_motion(x, y)







