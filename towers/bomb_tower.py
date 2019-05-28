from .tower import Tower
from settings import bomb_tower_width, bomb_tower_height, bomb_tower_icon
from projectiles import Bomb
import pygame


upgrade_definition_1 = {
    "price" : 8,
    "attack_speed" : 35,
    "range" : 150,
    "attack" : 15,
    "level" : '2'
}

updage_definition_2 = {
    "price" : 16,
    "attack_speed" : 30,
    "range" : 175,
    "attack" : 20,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 32,
    "attack_speed" : 25,
    "range" : 200,
    "attack" : 25,
    "level" : '4'
}


class BombTower(Tower):
    price = 8
    width = bomb_tower_width
    height = bomb_tower_height
    icon = bomb_tower_icon
    unlock_level = 3
    base_icon_path = "bomb_tower"
    description = '''
    a slow firing, 
    medium damage tower
    that deals damage 
    in a radius
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, bomb_tower_width, bomb_tower_height, bomb_tower_icon)

        # Attributes
        self.range = 100
        self.attack_speed = 40
        self.attack = 20
        self.projectile_speed = 25
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = Bomb


        