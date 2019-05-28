from .tower import Tower
from projectiles import Arrow
import pygame, math, random
from settings import fruit_farm_width, fruit_farm_height, fruit_farm_icon
import environment


upgrade_definition_1 = {
    "level" : '2',
    "produce_time" : 80,
    "wait_time" : 80,
    "price" : 6,
}

updage_definition_2 = {
    "price" : 12,
    "produce_time" : 60,
    "wait_time" : 60,
    "produce_value" : 4,
    "level" : '3'
}
updage_definition_3 = {
    "price" : 24,
    "produce_value" : 4,
    "produce_time": 40,
    "wait_time" : 40,
    "level" : '4'
}



class FruitFarm(Tower):
    price = 4
    width = fruit_farm_width
    height = fruit_farm_height
    icon = fruit_farm_icon
    unlock_level = 6

    base_icon_path = "fruit_farm"
    description = '''
    fruit
    '''


    def __init__(self, map_, x, y):
        Tower.__init__(self, map_, x, y, fruit_farm_width, fruit_farm_height, fruit_farm_icon)

        # Attributes
        self.range = 75
        self.attack_speed = 0
        self.attack = 0
        self.projectile_speed = 0
        self.upgrades = {
            "2" : upgrade_definition_1,
            "3" : updage_definition_2,
            "4" : updage_definition_3
        }
        self.projectile_class = Arrow

        # Fruit farm specific attributes
        self.produce_value = 3
        self.produce_time = 100
        self.wait_time = self.produce_time
        self.produced_fruit = []


    def try_attack(self):
        if (self.map.round.is_started):
            # print('trying to produce')
            if (self.wait_time <= 0):
                self.produce_fruit()
                self.wait_time = self.produce_time
            else:
                self.wait_time -= 1


    def produce_fruit(self):

        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = self.range * math.sqrt(random.random())
        x = r * math.cos(alpha) + self.x
        y = r * math.sin(alpha) + self.y

        fruit = Fruit(self.map, x, y, self.produce_value, self)
        self.produced_fruit.append(fruit)

    def render(self):
        environment.Game.screen.blit(self.get_icon(), (self.x, self.y))
        for fruit in self.produced_fruit:
            fruit.render()


    def handle_mouse_motion(self, x, y):
        if (self.is_dragging):
            self.x, self.y = x, y
        for fruit in self.produced_fruit:
            fruit.handle_mouse_motion(x, y)


        
class Fruit():

    icon = pygame.transform.scale(pygame.image.load("images/fruit.png"), (20, 20))

    def __init__(self, map_, x, y, value, farm):
        self.map = map_
        self.x = x
        self.y = y
        self.value = value
        self.width = 20
        self.height = 20
        self.farm = farm

    def render(self):
        environment.Game.screen.blit(self.icon, (self.x, self.y))

    def handle_mouse_motion(self, x, y):
        if (x <= (self.x + self.width) and x >= self.x
            and y <= (self.y + self.height) and y >= self.y):
            environment.Game.player.sell(self.value)
            self.farm.produced_fruit.remove(self)
            