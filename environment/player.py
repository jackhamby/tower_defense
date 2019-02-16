
import pygame


class Player():


    def __init__(self, game):
        self.game = game

        # Attributes
        self.gold = 10
        self.health = 100
        
        print('player created')

    def purchase(self, price):
        if (self.gold - price >= 0):
            self.gold -= price
            return True
        return False