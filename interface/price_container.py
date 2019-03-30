
import pygame
from .interface import Interface
import environment
from . import upgrade_button
from settings import price_container_height, price_container_width, price_container_icon
import math

# width = width
# height = math.floor(height * 0.35) 
# icon = pygame.transform.scale( pygame.image.load("images/container.png"), (width, price_container_height))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


class PriceContainer(Interface):

    def __init__(self, map_, x, y, price):
        Interface.__init__(self, map_, x, y, price_container_width, price_container_height, price_container_icon)
        self.price = price

    def render(self):
        pass
        # price_icon_y = self.y + self.height
        environment.Game.screen.blit(self.icon, (self.x, self.y))
        # self.game.screen.blit(self.price_container, (self.x, price_icon_y))
        textsurface = myfont.render(f'${self.price}', False, (0, 0, 0))
        text_x = self.x + math.floor(self.width * .1)
        text_y = self.y + math.floor(self.height * .01)
        environment.Game.screen.blit(textsurface,(text_x, text_y))
