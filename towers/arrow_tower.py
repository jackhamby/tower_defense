from .tower import Tower
from projectiles import Arrow
import pygame, math
from settings import arrow_tower_width, arrow_tower_height, arrow_tower_icon



upgrade_definition_1 = {
    "level" : '2',
    "price" : 6,
    "attack_speed" : 40,
    "range" : 250,
    "attack" : 60
}

updage_definition_2 = {
    "price" : 12,
    "attack_speed" : 30,
    "range" : 275,
    "attack" : 80,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 24,
    "attack_speed" : 20,
    "range" : 300,
    "attack" : 90,
    "level" : '4'
}



class ArrowTower(Tower):
    price = 4
    width = arrow_tower_width
    height = arrow_tower_height
    icon = arrow_tower_icon
    base_icon_path = "arrow_tower"


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, arrow_tower_width, arrow_tower_height, arrow_tower_icon)

        # Attributes
        self.range = 200
        self.attack_speed = 50
        self.attack = 50
        self.projectile_speed = 20
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = Arrow


        
