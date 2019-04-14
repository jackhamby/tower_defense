from .effect import Effect
import pygame
import environment 
import math

class Dot(Effect):

    def __init__(self, map_, target_x, target_y, damage_over_time):
        Effect.__init__(self, map_, target_x, target_y)
        self.damage_over_time = damage_over_time
        self.duration = 200
        self.enemy = None

    def apply(self, enemy):
        print('applied dot!')
        self.enemy = enemy
        enemy.effects.append(self)
        

    def tick(self):
        if (self.duration <= 0):
            self.enemy.effects.remove(self)
        else:
            if (self.duration % 20 == 0):
                self.enemy.take_damage(self.damage_over_time)
            self.duration -= 1
