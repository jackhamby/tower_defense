import pygame
import math

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Tile():
    

    def __init__(self, mapp, x, y):
        self.map = mapp
        self.game = mapp.game
        self.height = math.floor(SCREEN_HEIGHT / self.map.height)
        self.width = math.floor(SCREEN_WIDTH / self.map.width)
        self.x_index = x
        self.y_index = y
        self.x = self.width * x
        self.y = self.height * y
        self.unit = None

        



class PathTile(Tile):

    def __init__(self, mapp, x, y, is_start=False, is_end=False):
        Tile.__init__(self, mapp, x, y)
        self.is_start = is_start
        self.is_end = is_end
        # if (is_end):
        #     print(f'ending tile! {x}, {y}')
        # if (is_start):
        #     print(f'starting tile! {x}, {y}')


    def render(self):
        pygame.draw.rect(self.map.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))


class GroundTile(Tile):

    def __init__(self, mapp, x, y):
        Tile.__init__(self, mapp, x, y)
        # TODO: make as static memeber to avoid multiple image loads
        self.icon = pygame.transform.scale( pygame.image.load("images/ground_grass.png"), (self.width, self.height))


    def render(self):
        # pygame.draw.rect(self.map.game.screen, (255, 222, 173), (self.x, self.y, self.width, self.height))
        self.game.screen.blit(self.icon, (self.x, self.y))
