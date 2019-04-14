import pygame
from enemies import KingKobold, Kobold, Knight, Goblin
from threading import Thread
from time import sleep


class Round():
    ''' - keeps track of the current round
        - starts and stops rounds
        - keeps track of rounds's enemies 
        - spawns enemies '''

    def __init__(self, map_, level):
        self.level = level
        self.map = map_
        self.level = level
        self.enemy_pool = self.get_enemy_pool(level) 
        self.is_started = False

    def start(self):
        ''' start the round, create seperate thread for spawning enemies ''' 
        spawning_thread = Thread(target=self.spawn_enemies)
        spawning_thread.start()
        self.is_started = True

    def stop(self):
        ''' end the round '''
        self.map.round = Round(self.map, self.level + 1)

    def spawn_enemies(self):
        ''' thread function, remove enemies from enemy pool
            and send them to Map to be rendered  '''
        while(len(self.enemy_pool) > 0):
            enemy = self.enemy_pool.pop()
            self.map.enemies.append(enemy)
            enemy.spawn() 
            sleep(.5)

    def get_enemy_pool(self, level):
        ''' THIS WILL CHANGE
            hardcoded values for 5 Rounds of tower_defense  '''
        if (level == 1):
            return [Kobold(self.map) for i in range(6)] 
        elif(level == 2):
            return [Kobold(self.map) for i in range(8)] + [Knight(self.map) for i in range(3)] + [Goblin(self.map) for i in range(1)]
        elif(level == 3):
            return [KingKobold(self.map)] + [Kobold(self.map) for i in range(8)] + [Goblin(self.map) for i in range(2)]
        elif(level == 4): 
            return [KingKobold(self.map)] + [Knight(self.map) for i in range(10)] + [Kobold(self.map) for i in range(4)] + [KingKobold(self.map)]+ [Goblin(self.map) for i in range(4)]
        elif(level == 5):
            return  [KingKobold(self.map) for i in range(6) ] + [Knight(self.map) for i in range(15)] + [Goblin(self.map) for i in range(7)]
        else:
            return []
