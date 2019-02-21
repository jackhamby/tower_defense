import pygame
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

class TowerDetail():

    def __init__(self, game):
        self.game = game
        self.width = math.floor(SCREEN_WIDTH * 0.4)
        self.height = math.floor(SCREEN_HEIGHT * 0.1)
        self.display_attributes = ["health", "gold"]
        self.margin = 25
        self.text_margin = 5
        self.x = SCREEN_WIDTH - self.width
        self.y = SCREEN_HEIGHT - self.height
        self.selected_tower = None

        self.upgrade_buttons = []

        # self.buttons = [StartButton(self)]

    def set_upgrade_icons(self):
        # print('setting icons')
        self.upgrade_buttons = []
        inc =  math.floor(self.width * .20)
        x = self.x + math.floor(0.3 * self.width)
        y = self.y + math.floor(0.1 * self.height)
        for upgrade in self.selected_tower.upgrades:
            upgrade_button = UpgradeButton(self, upgrade, x, y)
            x += inc
            self.upgrade_buttons.append(upgrade_button, )


    def render(self):
        textsurface = myfont.render(f'Upgrades', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x, self.y - (self.text_margin * 6)))

        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, self.width - self.margin, self.height))
        if (self.selected_tower):
            # Show attack
            textsurface = myfont.render(f'attack {self.selected_tower.attack}', False, (255, 255, 255))
            self.game.screen.blit(textsurface,(self.x + self.text_margin,self.y + self.text_margin))

            # Show speed
            textsurface = myfont.render(f'speed {self.selected_tower.attack_speed}', False, (255, 255, 255))
            self.game.screen.blit(textsurface,(self.x + self.text_margin, self.y + (self.text_margin * 6)))

            # Show upgrade buttns
            for upgrade_button in self.upgrade_buttons:
                if (upgrade_button.upgrade in self.selected_tower.upgrades):
                    upgrade_button.render()


    def handle_mouse_down(self, x, y):
        for button in self.upgrade_buttons:
            button.handle_mouse_down(x, y)
        pass


    def handle_mouse_up(self, x, y):
        pass




class UpgradeButton():

    def __init__(self, tower_detail, upgrade, x, y):
        self.game = tower_detail.game
        self.tower_detail = tower_detail
        self.width = math.floor(tower_detail.width * .10)
        self.height = math.floor(tower_detail.height * .50)
        self.x = x
        self.y = y
        self.upgrade = upgrade


    def render(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        textsurface = myfont.render(f'${self.upgrade["price"]}', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x, (self.y + self.height) + self.tower_detail.text_margin))

    def handle_mouse_down(self, x, y):
        # pass
        if ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y):
             if (self.game.player.purchase(self.upgrade['price'])):
                # print('purchased upgrade!!!!')
                self.apply_upgrade()

    def apply_upgrade(self):
        
        for attribute, upgrade_value in self.upgrade.items():
            if (attribute == "price"):
                continue
            previous_value = getattr(self.tower_detail.selected_tower, attribute)
            upgraded_value = previous_value + upgrade_value
            # print(self.upgrade)
            # print(self.tower_detail.selected_tower.level)
            # self.tower_detail.selected_tower.upgrades.remove(self.upgrade)
            setattr(self.tower_detail.selected_tower, attribute, upgraded_value)
        self.tower_detail.selected_tower.level = self.upgrade['level']
        self.tower_detail.selected_tower.upgrades.remove(self.upgrade)

    def handle_mouse_up(self, x, y):
        pass
        # self.x, self.y = x, y
        # if (self.selected_tower):
        #     self.selected_tower.x, self.selected_tower.y = x, y
        #     self.selected_tower.dragging = False
        #     self.selected_tower = None
             


    
