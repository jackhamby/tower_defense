from .tower import Tower
from projectiles import BoostWave
import pygame, math
from settings import boost_tower_width, boost_tower_height, boost_tower_icon



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



class BoostTower(Tower):
    price = 4
    width = boost_tower_width
    height = boost_tower_height
    icon = boost_tower_icon
    unlock_level = 7
    base_icon_path = "boost_tower"
    description = '''
    boost
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, boost_tower_width, boost_tower_height, boost_tower_icon)

        # Attributes
        self.range = 200
        self.attack_speed = 0
        self.attack = 0
        self.projectile_speed = 20
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }

        self.boost_value = 10
        self.boost_attribute = "attack_speed"

        self.projectile_class = BoostWave



    def try_attack(self):
        # print('trying attack')
        self.boost_wave = self.projectile_class(self.map, self.x, self.y, self.boost_attribute, self.boost_value, self)
        for tower in self.map.towers:
            if (tower == self):
                continue
            if (self.in_range(tower)):
                self.try_apply(tower)

                    # # If tower hasnt been effected the boost tower yet
                    # for tower_effect in tower.effects:
                    #     if (tower_effect.source_tower != self):
                    #         print('appending effect to tower')
                    #         print(tower)
                    #         tower.effects.append(effect) 


    def try_apply(self, tower):
        for tower_effect in tower.effects:
            if (tower_effect.source_tower == self):
                return
        tower.effects.append(self.boost_wave.effects[0])

                    




    def in_range(self, tower):
        if (math.sqrt(pow(self.x - tower.x, 2) + pow(self.y - tower.y, 2)) <= self.range):
            return True
        else:
            return False
            
        
    # def init_effects(self):
    #     self.effects = [Boost(self.map, self.x, self.y, self.boost_value, self.boost_attribute, self.range)]
