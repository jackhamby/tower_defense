
from .tower import Tower



upgrade_definition_1 = {
    "price" : 2,
    "attack_speed" : -10,
    "range" : 50,
    "attack" : 15
}

updage_definition_2 = {
    "price" : 7,
    "attack_speed" : -20,
    "range" : 100,
    "attack" : 25
}
updage_definition_3 = {
    "price" : 15,
    "attack_speed" : -30,
    "range" : 300,
    "attack" : 50
}


class ArrowTower(Tower):
    price = 2

    def __init__(self, game, x, y):
        Tower.__init__(self, game, x, y)

        # Attributes
        self.range = 200
        self.attack_speed = 80
        self.width = 20
        self.height = 50
        self.attack = 25
        self.projectile_speed = 20

        self.upgrades = [upgrade_definition_1, updage_definition_2, updage_definition_3]


        
