from .tower import Tower
from settings import magic_tower_width, magic_tower_height, magic_tower_icon
from projectiles import Lightning
import pygame


upgrade_definition_1 = {
    "price" : 8,
    "attack_speed" : 10,
    "range" : 150,
    "attack" : 15,
    "level" : '2'
}

updage_definition_2 = {
    "price" : 16,
    "attack_speed" : 7,
    "range" : 175,
    "attack" : 25,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 32,
    "attack_speed" : 5,
    "range" : 200,
    "attack" : 30,
    "level" : '4'
}


class MagicTower(Tower):
    price = 4
    width = magic_tower_width
    height = magic_tower_height
    icon = magic_tower_icon
    unlock_level = 2

    base_icon_path = "magic_tower"
    description = '''
    a fast shooting,
    low damage tower
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, magic_tower_width, magic_tower_height, magic_tower_icon)

        # Attributes
        self.range = 100
        self.attack_speed = 10
        self.attack = 10
        self.projectile_speed = 25
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = Lightning


        