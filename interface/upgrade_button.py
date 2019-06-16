from .interface import Interface
from .price_container import PriceContainer
import environment
import pygame
import math
from settings import upgrade_button_width, upgrade_button_height, upgrade_button_icon, tower_upgrade_icon_margin

class UpgradeButton(Interface):

    def __init__(self, map_, x, y, tower, upgrade):
        Interface.__init__(self, map_, x, y, upgrade_button_width, upgrade_button_height, upgrade_button_icon)
        self.tower = tower
        self.upgrade = upgrade
        self.price_container = PriceContainer(map_, self.x, self.y + self.height, upgrade['price'])


    def render(self):
        environment.Game.screen.blit(self.icon, (self.x, self.y))
        # Render tower icon for upgrade

        # if (len(self.map.selected_tower.upgrades.keys()) != self.upgrade["level"])
        # if (self.tower.upgrades > self.map.round.level and not in_development_mode):
        #     locked_icon = pygame.transform.scale( pygame.image.load("images/locked_icon.png"), (rect_width, rect_height))
        #     self.screen.blit(locked_icon, (self.x, self.y))
        #     return 

        tower_icon_x = self.x + math.floor(self.width / 2) - math.floor(self.tower.width / 2)
        tower_icon_y = self.y + math.floor(self.height * .25)
        environment.Game.screen.blit(self.tower.get_icon(f'{self.tower.base_icon_path}{self.upgrade["level"]}.png'), (tower_icon_x, tower_icon_y))
        # Render price conainer
        self.price_container.render()

    def handle_mouse_down(self, x, y):
        # pass
        if ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y):
             print('upgraded')
            #  print(self.upgra)
             if (environment.Game.player.purchase(self.upgrade['price'])):
                self.apply_upgrade()
                # print('upgraddeeee')

    def apply_upgrade(self):
        print('apply upraged')
        # pass
        for attribute, upgrade_value in self.upgrade.items():
            if (attribute == "price"):
                continue
            setattr(self.map.selected_tower, attribute, upgrade_value)
        self.map.selected_tower.level = self.upgrade['level']
        del self.map.selected_tower.upgrades[self.upgrade['level']]
        self.map.tower_detail.upgrade_buttons.remove(self)



