import sys, pygame
from .map import Map
from .player import Player
from enemies import Enemy, Kobold, KingKobold
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
        self.clock = pygame.time.Clock()
    
    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for component in self.interface_components:
                        component.handle_mouse_down(x, y)
                    for tower in self.map.towers:
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
            if (self.round.is_started and len(self.round.enemy_pool) == 0 and len(self.round.enemies) == 0):
                self.round.stop()
            pygame.display.flip()
            self.clock.tick(360)


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
        self.enemies = []
        self.enemy_pool = self.get_enemy_pool(level) 
        self.is_started = False

    def start(self):
        spawning_thread = Thread(target=self.spawn_enemies)
        spawning_thread.start()
        self.is_started = True

    def stop(self):
        self.game.round = Round(self.game, self.level + 1)
        print('stop round')

    def spawn_enemies(self):
        while(len(self.enemy_pool) > 0):
            enemy = self.enemy_pool.pop()
            self.enemies.append(enemy)
            enemy.spawn()
            sleep(1.0)
        # for enemy in self.enemy_pool:
            # self.enemies.append(self.enemy_pool.pop())
            # print('spawn')


    def get_enemy_pool(self, level):
        if (level == 1):
            return [Kobold(self) for i in range(4)]
        elif(level == 2):
            return [Kobold(self) for i in range(8)]
        elif(level == 3):
            return [KingKobold(self)]
        elif(level == 4): 
            return [KingKobold(self)] + [Kobold(self) for i in range(4)] + [KingKobold(self)]
        elif(level == 5):
            return [KingKobold(self) for i in range(6) ]
        else:
            return []




        # pass

