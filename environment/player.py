
import pygame


class Player():


    def __init__(self):

        # Attributes
        self.gold = 10
        self.health = 100
        
    def purchase(self, price):
        # print(self.gold)
        # print(price)
        if (self.gold - price >= 0):
            self.gold -= price
            return True
        return False