from .tower import Tower
import pygame


upgrade_definition_1 = {
    "price" : 2,
    "attack_speed" : 10,
    "range" : 150,
    "attack" : 15,
    "level" : '2'
}

updage_definition_2 = {
    "price" : 7,
    "attack_speed" : 0,
    "range" : 175,
    "attack" : 25,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 15,
    "attack_speed" : 0,
    "range" : 200,
    "attack" : 30,
    "level" : '4'
}

icon = pygame.transform.scale( pygame.image.load("images/magic_tower1.png"), (25, 40))


class MagicTower(Tower):
    price = 2
    icon = icon
    base_icon_path = "magic_tower"


    def __init__(self, game, x, y):
        Tower.__init__(self, game, x, y)

        # Attributes
        self.range = 100
        self.attack_speed = 10
        self.width = 25
        self.height = 40
        self.attack = 10
        self.projectile_speed = 25
        self.icon = icon



        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }


        