import pygame, math
from towers import ArrowTower, MagicTower, Tower

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


class TowerSelect():

    def __init__(self, game):
        self.game = game
        self.width = math.floor(SCREEN_WIDTH * 0.4)
        self.height = math.floor(SCREEN_HEIGHT * 0.1)
        self.x = 0 
        self.text_margin = 5
        self.y = SCREEN_HEIGHT - self.height
        self.tower_icons = [TowerIcon(self, ArrowTower), TowerIcon(self, MagicTower)]


    def render(self):
        textsurface = myfont.render(f'Shop', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x, self.y - (self.text_margin * 6)))
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        inc =  math.floor(self.width * .20)
        x = self.x + math.floor(0.1 * self.width)
        y =  self.y + math.floor(0.1 * self.height)
        for icon in self.tower_icons:
            icon.render(x, y)
            x += inc


    def handle_mouse_down(self, x, y):
        for icon in self.tower_icons:
            icon.handle_mouse_down(x, y)

    def handle_mouse_up(self, x, y):
        for icon in self.tower_icons:
            icon.handle_mouse_up(x, y)
        # pass







class TowerIcon():
    
    def __init__(self, tower_select, tower):
        self.tower = tower
        self.game = tower_select.game
        self.tower_select = tower_select
        self.width = math.floor(tower_select.width * .10)
        self.height = math.floor(tower_select.height * .50)
        # self.x = self.tower_select.x + math.floor(0.1 * self.tower_select.width)
        # self.y = self.tower_select.y + math.floor(0.1 * self.tower_select.height)
        self.selected_tower = None


    def render(self, x, y):
        self.x = x
        self.y = y
        # pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.game.screen.blit(self.tower.icon, (self.x, self.y))

        textsurface = myfont.render(f'${self.tower.price}', False, (255, 255, 255))
        self.game.screen.blit(textsurface,(self.x, (self.y + self.height) + self.tower_select.text_margin))
    
    def handle_mouse_down(self, x, y):
        if ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y):
             if (self.game.player.purchase(self.tower.price)):
                # print('creating tower')
                tower = self.tower(self.game, x, y)
                tower.dragging = True
                self.selected_tower = tower
                self.game.map.towers.append(tower)
                # print(self.game.map.towers)


    def handle_mouse_up(self, x, y):
        # self.x, self.y = x, y
        if (self.selected_tower):
            self.selected_tower.x, self.selected_tower.y = x, y
            self.selected_tower.dragging = False
            self.selected_tower = None
             


    
