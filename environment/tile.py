import pygame
import math

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Tile():

    def __init__(self, mapp, x, y):
        self.map = mapp
        self.height = math.floor(SCREEN_HEIGHT / self.map.height)
        self.width = math.floor(SCREEN_WIDTH / self.map.width)
        self.x = self.width * x
        self.y = self.height * y
        self.unit = None

        



class PathTile(Tile):

    def __init__(self, mapp, x, y):
        Tile.__init__(self, mapp, x, y)

    def render(self):
        pygame.draw.rect(self.map.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

        pass


class GroundTile(Tile):

    def __init__(self, mapp, x, y):
        Tile.__init__(self, mapp, x, y)

    def render(self):
        pygame.draw.rect(self.map.game.screen, (255, 222, 173), (self.x, self.y, self.width, self.height))

        pass