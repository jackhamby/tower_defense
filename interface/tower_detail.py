import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 800
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

class TowerDetail():


    width = SCREEN_WIDTH
    height = math.floor(SCREEN_HEIGHT * .125)
    icon = pygame.transform.scale( pygame.image.load("images/stonewall.png"), (width, height))
    x = 0
    y = SCREEN_HEIGHT - height

    def __init__(self, game):
        self.game = game
        self.selected_tower = None
        self.upgrade_buttons = []
        self.tower_icon = None


    def set_upgrade_icons(self):
        print('setting icons')
        self.upgrade_buttons = []
        self.tower_icon = TowerIcon(self, self.selected_tower)
        for upgrade_level, upgrade in self.selected_tower.upgrades.items():
            upgrade_button = UpgradeButton(self, upgrade)
            self.upgrade_buttons.append(upgrade_button)



    def render(self):
        self.game.screen.blit(self.icon, (self.x, self.y))

        if (self.selected_tower):
            margin = math.floor(SCREEN_WIDTH * .01)
            # Render Tower icon
            self.tower_icon.render(self.x + margin, self.y + margin)


            x = (self.x + margin + self.tower_icon.width) + (margin * 4)
            y = self.y + margin

            # Show upgrade buttns
            for upgrade_button in self.upgrade_buttons:
                upgrade_button.render(x, y)
                x += upgrade_button.width + (margin * 4)
        


    def handle_mouse_down(self, x, y):
        for button in self.upgrade_buttons:
            button.handle_mouse_down(x, y)


    def handle_mouse_up(self, x, y):
        pass




class TowerIcon():


    def __init__(self, tower_detail, tower):
        self.tower_detail = tower_detail
        self.game = tower_detail.game
        self.tower = tower
        self.height = math.floor(tower_detail.height * .85)
        self.width = math.floor(tower_detail.width * .10)
        # TODO: make as a static member to avoid loading imgs often
        self.icon =  pygame.transform.scale( pygame.image.load("images/icon_container.png"), (self.width, self.height))

    def render(self, x, y):
        self.x = x
        self.y = y
        self.game.screen.blit(self.icon, (self.x, self.y))
        tower_icon_x = self.x + math.floor(self.width / 2) - math.floor(self.tower.width / 2)
        tower_icon_y = self.y + math.floor(self.height * .25)
        self.game.screen.blit(self.tower.icon, (tower_icon_x, tower_icon_y))




class UpgradeButton():

    def __init__(self, tower_detail, upgrade):
        self.game = tower_detail.game
        self.tower_detail = tower_detail
        self.width = math.floor(tower_detail.width * .062)
        self.height = math.floor(tower_detail.height * .62)
        self.tower = tower_detail.selected_tower
        self.price_container_height = math.floor(self.height * 0.35) 

        self.icon =  pygame.transform.scale( pygame.image.load("images/icon_container.png"), (self.width, self.height))
        self.price_container = pygame.transform.scale( pygame.image.load("images/container.png"), (self.width, self.price_container_height))

        self.upgrade = upgrade


    def render(self, x, y):
        self.x = x
        self.y = y 
        self.game.screen.blit(self.icon, (self.x, self.y))

        # Render tower icon for upgrade
        tower_icon_x = self.x + math.floor(self.width / 2) - math.floor(self.tower.width / 2)
        tower_icon_y = self.y + math.floor(self.height * .25)
        self.game.screen.blit(self.tower.get_icon(f'{self.tower.base_icon_path}{self.upgrade["level"]}.png'), (tower_icon_x, tower_icon_y))

        # Render price window 
        price_icon_y = self.y + self.height
        self.game.screen.blit(self.price_container, (self.x, price_icon_y))
        textsurface = myfont.render(f'${self.upgrade["price"]}', False, (0, 0, 0))
        text_x = self.x + math.floor(self.width * .1)
        text_y = price_icon_y + math.floor(self.height * .01)
        self.game.screen.blit(textsurface,(text_x, text_y))


    def handle_mouse_down(self, x, y):
        # pass
        if ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y):
             if (self.game.player.purchase(self.upgrade['price'])):
                self.apply_upgrade()

    def apply_upgrade(self):
        
        for attribute, upgrade_value in self.upgrade.items():
            if (attribute == "price"):
                continue
            setattr(self.tower_detail.selected_tower, attribute, upgrade_value)
        self.tower_detail.selected_tower.level = self.upgrade['level']
        del self.tower_detail.selected_tower.upgrades[self.upgrade['level']]
        self.tower_detail.upgrade_buttons.remove(self)

    def handle_mouse_up(self, x, y):
        pass

             


    
