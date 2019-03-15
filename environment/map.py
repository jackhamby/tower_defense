from .tile import Tile, GroundTile, PathTile
# from enemies import K
import math
import pygame

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

DEFAULT_LAYOUT = """9 8
11e111111
110111111
110000011
111111011
111111011
111100011
111101111
1111s1111"""

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Map():

    def __init__(self, game, layout=DEFAULT_LAYOUT):
        self.game = game
        self.width = -1
        self.height = -1
        self.map = None
        self.starting_tile = None
        self.ending_tile = None
        self.layout = layout
        self.load_layout()
        # self.current_round = None
        self.towers = []
        self.selected_tower = None
   
        # print('initalized map')


    def load_layout(self):
        self.map = []
        layout = self.layout.split('\n')
        self.width, self.height = [int(x) for x in layout.pop(0).split(' ')]
        for i in range(0, self.height):
            map_row = []
            layout_row = layout[i]
            for k, layout_tile in enumerate(list(layout_row)):
                if (layout_tile == "1"):
                    map_row.append(GroundTile(self, k, i)) # Ground tile
                elif(layout_tile == "0"):
                    map_row.append(PathTile(self, k, i)) # Path tile
                elif(layout_tile == "s"):
                    self.starting_tile = PathTile(self, k, i, is_start=True)
                    map_row.append(self.starting_tile) # Starting tile
                elif(layout_tile == "e"):
                    self.ending_tile = PathTile(self, k, i, is_end=True)
                    map_row.append(self.ending_tile) # Ending tile        
            self.map.append(map_row)

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
        if (self.game.round):
            for enemy in self.game.round.enemies:
                enemy.render()








