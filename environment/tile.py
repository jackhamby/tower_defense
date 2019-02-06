import pygame
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Tile():

    def __init__(self, mapp, x, y):
        self.map = mapp
        self.height = math.floor(SCREEN_HEIGHT / self.map.height)
        self.width = math.floor(SCREEN_WIDTH / self.map.width)
        self.x = self.width * x
        self.y = self.height * y
        if self.y == 0:
            print(self.x)

        # print(f'width: {self.width}, height: {self.height}')

    # def render(self):
        # pygame.draw.rect(self.map.game.screen, (255, 0, 255), (self.x, self.y, self.width, self.height))




class PathTile(Tile):

    def __init__(self, mapp, x, y):
        Tile.__init__(self, mapp, x, y)

    def render(self):
        pygame.draw.rect(self.map.game.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

        pass


class GroundTile(Tile):

    def __init__(self, mapp, x, y):
        Tile.__init__(self, mapp, x, y)

    def render(self):
        pygame.draw.rect(self.map.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

        pass