from .interface import Interface
from settings import data_display_width, data_display_height
import math
import environment
import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

class DataDisplay(Interface):
    def __init__(self, map_, attribute_name, x, y):
        icon = pygame.transform.scale( pygame.image.load(f'images/input_{attribute_name}.png'), (data_display_width, data_display_height))
        Interface.__init__(self, map_, x, y, data_display_width, data_display_height, icon )
        self.screen = environment.Game.screen
        self.attribute = attribute_name

    def render(self):
        # self.x = x
        # self.y = y
        # pygame.transform.scale(self.icon, (self.width, self.height))
        self.screen.blit(self.icon, (self.x, self.y))

        textsurface = myfont.render(f'{getattr(environment.Game.player, self.attribute)}', False, (0, 0, 0))
        self.screen.blit(textsurface,(self.x + math.floor(self.width * .3), self.y + math.floor(self.height * .1)))
    
        # Render data 

