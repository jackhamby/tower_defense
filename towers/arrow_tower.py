from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .tower import Tower
import pygame, math


upgrade_definition_1 = {
    "level" : '2',
    "price" : 2,
    "attack_speed" : 40,
    "range" : 250,
    "attack" : 60
}

updage_definition_2 = {
    "price" : 7,
    "attack_speed" : 30,
    "range" : 275,
    "attack" : 80,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 15,
    "attack_speed" : 20,
    "range" : 300,
    "attack" : 90,
    "level" : '4'
}



class ArrowTower(Tower):
    price = 2
    width = math.floor(SCREEN_WIDTH * .025)
    height = math.floor(SCREEN_HEIGHT * .05)
    icon = pygame.transform.scale( pygame.image.load("images/arrow_tower1.png"), (width, height))
    base_icon_path = "arrow_tower"


    def __init__(self, game, x, y):
        Tower.__init__(self, game, x, y)

        # Attributes
        self.range = 200
        self.attack_speed = 50
        # self.width = 25
        # self.height = 40
        self.attack = 50
        self.projectile_speed = 20
        # icon = pygame.transform.scale( pygame.image.load("images/arrow_tower1.png"), (25, 40))
        # self.icon = icon

        # @property
        # def icon(self):
        #     print(self.level)
        #     return pygame.transform.scale( pygame.image.load(f'images/arrow_tower{self.level}.png'), (25, 40))

        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        # self.upgrades = [upgrade_definition_1, updage_definition_2, updage_definition_3]


        
