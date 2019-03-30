from .interface import Interface
from .price_container import PriceContainer
import pygame
import environment
import math
from settings import tower_upgrade_icon_width, tower_upgrade_icon_height, tower_upgrade_icon_icon, tower_upgrade_icon_x, tower_upgrade_icon_y

class TowerUpgradeIcon(Interface):

    def __init__(self, map_, tower):
        Interface.__init__(self, map_, tower_upgrade_icon_x, tower_upgrade_icon_y, tower_upgrade_icon_width, tower_upgrade_icon_height, tower_upgrade_icon_icon)
        self.tower = tower

    def render(self):
        environment.Game.screen.blit(self.icon, (self.x, self.y))

        # Render tower icon for upgrade
        tower_icon_x = self.x + math.floor(self.width / 2) - math.floor(self.tower.width / 2)
        tower_icon_y = self.y + math.floor(self.height * .25)
        environment.Game.screen.blit(self.tower.icon, (tower_icon_x, tower_icon_y))

