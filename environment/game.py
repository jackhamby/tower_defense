import sys, pygame
from .map import Map
from .player import Player
from enemies import Enemy, Kobold
from interface import TowerSelect, Menu, PlayerDisplay, TowerDetail
from time import sleep
from threading import Thread

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

enemy_count = 10

class Game():

    def __init__(self, map_width=9, map_height=8):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.map = Map(self)
        self.interface_components = [TowerSelect(self), Menu(self), PlayerDisplay(self), TowerDetail(self)]
        self.round = Round(self, 1)
        self.player = Player(self)
    
    def start(self):
        self.map.current_round = self.round
        # self.round.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # print('mouse down')
                    for component in self.interface_components:
                        component.handle_mouse_down(x, y)
                    # print(self.map.towers)
                    for tower in self.map.towers:
                        # print('handling')
                        tower.handle_mouse_down(x, y)
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    for component in self.interface_components:
                        component.handle_mouse_up(x, y)
                    for tower in self.map.towers:
                        tower.handle_mouse_up(x, y)
                
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    for tower in self.map.towers:
                        tower.handle_mouse_motion(x, y)

            for tower in self.map.towers:
                tower.try_attack()
            self.render()
            pygame.display.flip()

    def render(self):
        self.map.render()
        for component in self.interface_components:
            component.render()


    def get_tower_detail(self):
        for component in self.interface_components:
            if type(component) == TowerDetail:
                return component
        return None



class Round():

    def __init__(self, game, level):
        self.level = level
        self.game = game
        self.map = game.map
        self.level = level
        self.enemies = [Kobold(self) for i in range(level * 10)]

    def start(self):
        spawning_thread = Thread(target=self.spawn_enemies)
        spawning_thread.start()

    def spawn_enemies(self):
        for enemy in self.enemies:
            enemy.spawn()
            sleep(1.0)

        # pass

