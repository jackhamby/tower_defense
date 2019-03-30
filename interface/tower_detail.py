import pygame
import math
from settings import tower_detail_width, tower_detail_height, tower_detail_x, tower_detail_y, tower_detail_icon, tower_upgrade_icon_margin
from .interface import Interface
from .tower_icon import TowerIcon
from .upgrade_button import UpgradeButton
from .tower_upgrade_icon import TowerUpgradeIcon
import environment
# Set fonts
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


class TowerDetail(Interface):

    def __init__(self, map_):
        Interface.__init__(self, map_, tower_detail_x, tower_detail_y, tower_detail_width, tower_detail_height, tower_detail_icon)
        self.screen = environment.Game.screen
        self.selected_tower = None
        self.upgrade_buttons = []
        self.tower_upgrade_icon = None
        


    def set_upgrade_icons(self):
        print('setting icons')
        self.upgrade_buttons = []
        self.tower_upgrade_icon = TowerUpgradeIcon(self.map, self.selected_tower)
            # def __init__(self, map_, x, y, tower, upgrade):
        upgrade_button_x = self.x + self.tower_upgrade_icon.width + (tower_upgrade_icon_margin * 2)
        upgrade_button_y = self.y + tower_upgrade_icon_margin
        for upgrade_level, upgrade in self.selected_tower.upgrades.items():
            upgrade_button = UpgradeButton(self.map, upgrade_button_x, upgrade_button_y, self.selected_tower, upgrade)
            self.upgrade_buttons.append(upgrade_button)
            upgrade_button_x += self.tower_upgrade_icon.width + tower_upgrade_icon_margin



    def render(self):
        self.screen.blit(self.icon, (self.x, self.y))

        if (self.selected_tower):
            self.tower_upgrade_icon.render()

            


        #     x = (self.x + margin + self.tower_icon.width) + (margin * 4)
        #     y = self.y + margin

            # Show upgrade buttns
            for upgrade_button in self.upgrade_buttons:
                upgrade_button.render()
                # x += upgrade_button.width + (margin * 4)
        


    def handle_mouse_down(self, x, y):
        for button in self.upgrade_buttons:
            button.handle_mouse_down(x, y)




             


    
