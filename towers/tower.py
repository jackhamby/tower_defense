import environment
import pygame
import math
from settings import arrow_tower_width, arrow_tower_height, arrow_tower_icon
from projectiles import Arrow

class Tower():
    description = '''
        a tower
    '''

    def __init__(self, map_, x, y, width, height, icon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.icon = icon
        self.map = map_

        self.level = 1
        self.is_dragging = False
        self.attack_wait = 0
        self.targeted_enemy = None
        self.fired_projectiles = []

        # Default attributes

        self.range = 200
        self.attack_speed = 80
        self.attack = 25
        self.projectile_speed = 20
        self.upgrades = {}
        self.projectile_class = Arrow



    def render(self):
        environment.Game.screen.blit(self.get_icon(), (self.x, self.y))
        for projectile in self.fired_projectiles:
            projectile.render()
    
    def fire_projectile(self):
        center_x = math.floor(self.x + (self.width / 2))
        center_y = math.floor(self.y + (self.height / 2))
        enemy_center_x = math.floor(self.targeted_enemy.x + (self.targeted_enemy.width / 2))
        enemy_center_y = math.floor(self.targeted_enemy.y + (self.targeted_enemy.height / 2))
        projectile = self.projectile_class(self.map, center_x, center_y, enemy_center_x, enemy_center_y, self.attack)
        # self.fired_projectiles.append(projectile)
        self.attack_wait = self.attack_speed
        projectile.fire(self.targeted_enemy)
        projectile.render()
        # self.fired_projectiles.append(projectile)
        # if (self.targeted_enemy):
        #     self.targeted_enemy.take_damage(self.attack)


    def try_attack(self):
        if (self.is_dragging):
            return
        if (self.attack_wait != 0):
            self.attack_wait -= 1
            return
        # No enemy in target, check for new target
        if (not self.targeted_enemy):
            for enemy in self.map.enemies:
                dist = math.sqrt(pow(self.x - enemy.x, 2) + pow(self.y - enemy.y, 2))
                # Check if enenmy is in range
                if (dist <= self.range):
                    self.targeted_enemy = enemy
                    self.fire_projectile()
                    break
        # # Already has a target which is alive
        elif(self.targeted_enemy.is_alive):
            dist = math.sqrt(pow(self.x - self.targeted_enemy.x, 2) + pow(self.y - self.targeted_enemy.y, 2))
            # Check if still in range
            if (dist >= self.range):
                self.targeted_enemy = None
            else:
                self.fire_projectile()

        # # Its current target died
        else:
            self.targeted_enemy = None
            return 


    def handle_mouse_down(self, x, y):
        # pass
        if (x >= self.x and x <= (self.x + self.width)  and
            y >= self.y and y <= (self.y + self.height) and 
            not self.is_dragging):
            self.map.selected_tower = self
            self.map.tower_detail.set_upgrade_icons()
            

    def handle_mouse_up(self, x, y):
        pass

    def remove(self):
        self.map.towers.remove(self)


    def handle_mouse_motion(self, x, y):
        if (self.is_dragging):
            # print('draggin!')
            self.x, self.y = x, y


    def get_icon(self, img_path=None):
        if (not img_path):
            img_path = f'{self.base_icon_path}{self.level}.png'
        return pygame.transform.scale( pygame.image.load(f'images/{img_path}'), (self.width, self.height))




