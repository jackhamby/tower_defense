from .tower import Tower
from settings import slime_tower_width, slime_tower_height, slime_tower_icon
from projectiles import Arrow
import pygame


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
    base_icon_path = "slime_tower"


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
        self.projectile_class = Arrow


        