from .tower import Tower
import pygame


upgrade_definition_1 = {
    "price" : 2,
    "attack_speed" : -10,
    "range" : 50,
    "attack" : 15,
    "level" : 1
}

updage_definition_2 = {
    "price" : 7,
    "attack_speed" : -20,
    "range" : 100,
    "attack" : 25,
    "level" : 2
}
updage_definition_3 = {
    "price" : 15,
    "attack_speed" : -30,
    "range" : 300,
    "attack" : 50,
    "level" : 3
}

icon = pygame.transform.scale( pygame.image.load("images/magic_tower1.png"), (25, 40))


class MagicTower(Tower):
    price = 2
    icon = icon

    def __init__(self, game, x, y):
        Tower.__init__(self, game, x, y)

        # Attributes
        self.range = 100
        self.attack_speed = 10
        self.width = 25
        self.height = 40
        self.attack = 5
        self.projectile_speed = 25
        self.icon = icon
        self.base_icon_path = "magic_tower"



        self.upgrades = [upgrade_definition_1, updage_definition_2, updage_definition_3]


        