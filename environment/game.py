import sys, pygame
from .map import Map
from .player import Player
from .round import Round
from enemies import Enemy, Kobold, KingKobold
from interface import TowerSelect, TowerDetail
from time import sleep

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

enemy_count = 10

class Game():
    ''' main pygame loop, wrapper for main game, includes Map and Player '''
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player()
    
    def __init__(self, map_width=9, map_height=8):
        # Map
        self.map = Map()

        # Player
        self.player = Player()

        self.clock = pygame.time.Clock()
    
    def start(self):
        ''' start main pygame loop, render game to screen'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.map.handle_mouse_down(x, y)
          
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    self.map.handle_mouse_up(x, y)
    
                
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    self.map.handle_mouse_motion(x, y)

            self.render()
            pygame.display.flip()
            # self.clock.tick(20)


    def render(self):
        ''' render Map to the screen '''
        self.map.render()


    # def get_tower_detail(self):
    #     for component in self.map.interface_components:
    #         if type(component) == TowerDetail:
    #             return component
    #     return None




