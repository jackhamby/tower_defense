
import pygame


class Player():
    ''' class for handling player data and player transactions '''

    def __init__(self):

        # Attributes
        self.gold = 100
        self.health = 100
        
    def purchase(self, price):
        ''' attempt to purchase an item given price'''
        # print(self.gold)
        # print(price)
        if (self.gold - price >= 0):
            self.gold -= price
            return True
        return False

    def sell(self, price):
        ''' gain money set by price '''
        self.gold += price