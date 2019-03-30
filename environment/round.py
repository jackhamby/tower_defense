import pygame
from enemies import KingKobold, Kobold
from threading import Thread
from time import sleep


class Round():

    def __init__(self, map_, level):
        self.level = level
        # self.game = game
        self.map = map_
        self.level = level
        self.enemy_pool = self.get_enemy_pool(level) 
        self.is_started = False

    def start(self):
        print('starting round')
        spawning_thread = Thread(target=self.spawn_enemies)
        spawning_thread.start()
        self.is_started = True

    def stop(self):
        self.map.round = Round(self.map, self.level + 1)
        print('stop round')

    def spawn_enemies(self):
        while(len(self.enemy_pool) > 0):
            enemy = self.enemy_pool.pop()
            self.map.enemies.append(enemy)
            enemy.spawn()
            sleep(1.0)

    def get_enemy_pool(self, level):
        if (level == 1):
            return [Kobold(self.map) for i in range(1)]
        elif(level == 2):
            return [Kobold(self.map) for i in range(8)]
        elif(level == 3):
            return [KingKobold(self.map)]
        elif(level == 4): 
            return [KingKobold(self.map)] + [Kobold(self.map) for i in range(4)] + [KingKobold(self.map)]
        elif(level == 5):
            return [KingKobold(self.map) for i in range(6) ]
        else:
            return []




        # pass