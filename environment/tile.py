import pygame
import math
import environment
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Tile():
    

    def __init__(self, width, height, x, y):
        ''' represents a square on the screen '''
        self.screen = environment.Game.screen
        self.height = height
        self.width = width
        self.x_index = x
        self.y_index = y
        self.x = self.width * x
        self.y = self.height * y
        self.unit = None

        



class PathTile(Tile):
    ''' Tile by which enemies can walk '''

    def __init__(self,  width, height, x, y, is_start=False, is_end=False):
        Tile.__init__(self, width, height, x, y)
        self.is_start = is_start
        self.is_end = is_end


    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))


class GroundTile(Tile):
    ''' Tile on which players can build towers '''

    def __init__(self, width, height, x, y):
        Tile.__init__(self, width, height, x, y)
        # TODO: make as static memeber to avoid multiple image loads
        self.icon = pygame.transform.scale(pygame.image.load("images/ground_grass.png"), (self.width, self.height))


    def render(self):
        self.screen.blit(self.icon, (self.x, self.y))
