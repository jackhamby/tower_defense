import sys, pygame
from .map import Map
from units import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Game():

    def __init__(self, map_width=9, map_height=8):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.map = Map(self)
        self.map.enemy = Enemy(self)
        self.map.enemy.spawn()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.render()
            pygame.display.flip()

    def render(self):
        self.map.render()
