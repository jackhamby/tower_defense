import pygame
import math
import environment


class Projectile():

    def __init__(self, map_,  x, y, target_x, target_y, damage):
        self.x, self.y = x, y
        self.map = map_
        self.target_x, self.target_y = target_x, target_y
        self.color = (0, 0, 0) # Default color
        self.flying = False
        self.damage = damage
        self.effects = []
        
    def fire(self, enemy):
        self.flying = True
        # if (self.targeted_enemy):
        enemy.take_damage(self.damage)
        for effect in self.effects:
            effect.apply(enemy)

    def die(self):
        self.flying = False

    def render(self):
        if (self.flying):
            pygame.draw.line(environment.Game.screen, self.color, (self.x, self.y), (self.target_x, self.target_y))
            self.die()


