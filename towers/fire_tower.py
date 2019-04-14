from .tower import Tower
from settings import fire_tower_width, fire_tower_height, fire_tower_icon
from projectiles import Fire
from effects import Dot
import pygame
import math


upgrade_definition_1 = {
    "price" : 8,
    "attack_speed" : 17,
    "range" : 150,
    "attack" : 12,
    "level" : '2'
}

updage_definition_2 = {
    "price" : 16,
    "attack_speed" : 15,
    "range" : 175,
    "attack" : 15,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 32,
    "attack_speed" : 13,
    "range" : 200,
    "attack" : 17,
    "level" : '4'
}


class FireTower(Tower):
    price = 8
    width = fire_tower_width
    height = fire_tower_height
    icon = fire_tower_icon
    base_icon_path = "fire_tower"
    description = '''
    an expensive low
    damage tower
    that deals damage 
    overtime
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, fire_tower_width, fire_tower_height, fire_tower_icon)

        # Attributes
        self.range = 100
        self.attack_speed = 20
        self.attack = 9
        self.projectile_speed = 25
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = Fire


        
    def try_attack(self):
        if (self.is_dragging):
            return
        if (self.attack_wait != 0):
            self.attack_wait -= 1
            return
        # No enemy in target, check for new target
        if (not self.targeted_enemy):
            enemies = self.get_in_range_enemies()
            if (len(enemies) == 0):
                return
            for enemy in enemies:
                if (self.check_if_on_fire(enemy)):
                    continue
                else:
                    self.targeted_enemy = enemy
                    self.fire_projectile()
                    self.targeted_enemy = None
                    return
            self.targeted_enemy = enemies[0]
            self.fire_projectile()
            self.targeted_enemy = None

    def check_if_on_fire(self, enemy):       
        for effect in enemy.effects:  # Skip already slowed enemies
            if (type(effect) == Dot):
                return True
        return False

    def get_in_range_enemies(self):
        in_range_enemies = []
        for i, enemy in enumerate(self.map.enemies):
            dist = math.sqrt(pow(self.x - enemy.x, 2) + pow(self.y - enemy.y, 2))
            # Check if enenmy is in range
            if (dist <= self.range):
                in_range_enemies.append(enemy)
        return in_range_enemies