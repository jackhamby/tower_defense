import pygame
import math
import environment


class Projectile():

    def __init__(self, x, y, target_x, target_y):
        # self.tower = tower
        # self.game = tower.game
        # self.targeted_enemy = tower.targeted_enemy
        self.x, self.y = x, y
        self.target_x, self.target_y = target_x, target_y
        self.color = (0, 0, 0) # Default color
        self.flying = False
        # self.width = 5
        # self.height = 5
        # self.speed = self.tower.projectile_speed
        
    def fire(self):
        print('fireing!')

        self.flying = True

    def die(self):
        self.flying = False
        # try:
        #     self.tower.fired_projectiles.remove(self)
        # except:
        #     print('failed to delete projectile')

    def render(self):
        if (self.flying):
            print('rendering?')
            pygame.draw.line(environment.Game.screen, self.color, (self.x, self.y), (self.target_x, self.target_y))
            self.die()
        # self.die()
        # if (self.flying and self.targeted_enemy.is_alive):
        #     enemy_center_x = self.targeted_enemy.x + math.floor(self.targeted_enemy.width / 2)
        #     enemy_center_y = self.targeted_enemy.y + math.floor(self.targeted_enemy.height / 2)
        #     # tower_center_x = self.
        #     pygame.draw.line(self.game.screen, (0, 0, 255), (self.x, self.y), (enemy_center_x, enemy_center_y))
        #     self.die()


