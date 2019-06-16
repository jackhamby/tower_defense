from .effect import Effect
import pygame
import environment 
import math

class Boost(Effect):

    def __init__(self, map_, boost_x, boost_y, attribute, amount, source_tower):
        Effect.__init__(self, map_, boost_x, boost_y)
        self.x, self.y = boost_x, boost_y
        self.amount = amount
        self.attribute = attribute
        self.source_tower = source_tower
        self.tower = None
        self.is_applied = False

    def apply(self, tower):
        
        if (not self.is_applied):
            self.tower = tower
            new_attr_value = getattr(tower, self.attribute) + self.amount
            setattr(tower, self.attribute, new_attr_value)
            print('increasing')
            self.is_applied = True
  
