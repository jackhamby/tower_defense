
from .tower import Tower
import pygame


upgrade_definition_1 = {
    "level" : 2,
    "price" : 2,
    "attack_speed" : -10,
    "range" : 50,
    "attack" : 15
}

updage_definition_2 = {
    "price" : 7,
    "attack_speed" : -20,
    "range" : 100,
    "attack" : 25,
    "level" : 3
}
updage_definition_3 = {
    "price" : 15,
    "attack_speed" : -30,
    "range" : 300,
    "attack" : 50,
    "level" : 4
}

icon = pygame.transform.scale( pygame.image.load("images/arrow_tower1.png"), (25, 40))


class ArrowTower(Tower):
    price = 2
    icon = icon

    def __init__(self, game, x, y):
        Tower.__init__(self, game, x, y)

        # Attributes
        self.range = 200
        self.attack_speed = 80
        self.width = 25
        self.height = 40
        self.attack = 25
        self.projectile_speed = 20
        self.base_icon_path = "arrow_tower"
        # icon = pygame.transform.scale( pygame.image.load("images/arrow_tower1.png"), (25, 40))
        # self.icon = icon

        # @property
        # def icon(self):
        #     print(self.level)
        #     return pygame.transform.scale( pygame.image.load(f'images/arrow_tower{self.level}.png'), (25, 40))


        self.upgrades = [upgrade_definition_1, updage_definition_2, updage_definition_3]


        
