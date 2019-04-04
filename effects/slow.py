from .effect import Effect
import pygame
import environment 
import math

class Slow(Effect):

    def __init__(self, map_, target_x, target_y, slow_amount):
        Effect.__init__(self, map_, target_x, target_y)
        self.amount = slow_amount
        self.duration = 200
        self.enemy = None

    def apply(self, enemy):
        self.enemy = enemy
        enemy.effects.append(self)
        enemy.speed -= self.amount
        if (enemy.speed <= 0):
            enemy.speed = 1
        

    def tick(self):
        if (self.duration <= 0):
            self.enemy.effects.remove(self)
            if (self.enemy.speed + self.amount > self.enemy.max_speed):
                self.enemy.speed = self.enemy.max_speed
            else:
                self.enemy.speed += self.amount
            
        else:
            self.duration -= 1
