from .effect import Effect
import pygame
import environment 
import math

class Explosion(Effect):

    def __init__(self, map_, target_x, target_y, damage, radius):
        Effect.__init__(self, map_, target_x, target_y)
        self.damage = damage
        self.radius = radius


    def apply(self, enemy):

        pygame.draw.circle(environment.Game.screen, (111, 111, 111), (self.target_x, self.target_y), self.radius, 2)
        # print(self.map.enemies)
        # print('\n')
        # print('\n')
        # print('\n')

        for enemy in self.map.enemies:
            if (self.check_in_radius(enemy)):
                enemy.take_damage(self.damage)
        # print('explosion!')
        # print('\n')
        # print('\n')
        # print('\n')

        pass

    def check_in_radius(self, enemy):
            dist = math.sqrt(pow(self.target_x - enemy.x, 2) + pow(self.target_y - enemy.y, 2))
            # # Check if still in range
            if (dist >= self.radius):
                return False
            return True