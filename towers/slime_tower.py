from .tower import Tower
from settings import slime_tower_width, slime_tower_height, slime_tower_icon
from projectiles import SlimeBall
from effects import Slow
import pygame
import math


upgrade_definition_1 = {
    "price" : 8,
    "attack_speed" : 15,
    "range" : 250,
    "attack" : 6,
    "level" : '2'
}

updage_definition_2 = {
    "price" : 16,
    "attack_speed" : 10,
    "range" : 175,
    "attack" : 7,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 32,
    "attack_speed" : 5,
    "range" : 200,
    "attack" : 8,
    "level" : '4'
}


class SlimeTower(Tower):
    price = 8
    width = slime_tower_width
    height = slime_tower_height
    icon = slime_tower_icon
    unlock_level = 4

    base_icon_path = "slime_tower"
    description = '''
    a fast shooting,
    low damage tower
    that slows its enemies
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, slime_tower_width, slime_tower_height, slime_tower_icon)

        # Attributes
        self.range = 200
        self.attack_speed = 20
        self.attack = 5
        self.projectile_speed = 25
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = SlimeBall


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
                if (self.check_if_slowed(enemy)):
                    continue
                else:
                    self.targeted_enemy = enemy
                    self.fire_projectile()
                    self.targeted_enemy = None
                    return
            self.targeted_enemy = enemies[0]
            self.fire_projectile()
            self.targeted_enemy = None

    def check_if_slowed(self, enemy):       
        for effect in enemy.effects:  # Skip already slowed enemies
            if (type(effect) == Slow):
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
                