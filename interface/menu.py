import pygame, math
from towers import Tower


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)



class Menu():

    def __init__(self, game):
        self.game = game
        self.width = math.floor(SCREEN_WIDTH * 0.25)
        self.height = math.floor(SCREEN_HEIGHT * 0.1)
        self.x = 25
        self.y = 25
        self.buttons = [StartButton(self)]
        # print(self.x, self.y)
        # self.tower_icons = [TowerIcon(self)]


    def render(self):
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        for button in self.buttons:
            button.render()
        # for icon in self.tower_icons:
        #     icon.render()

    # def handle_click(self, x, y):


    def handle_mouse_down(self, x, y):
        # pass
        for button in self.buttons:
            button.handle_mouse_down(x, y)

    def handle_mouse_up(self, x, y):
        pass
        # for icon in self.tower_icons:
        #     icon.handle_mouse_up(x, y)
        # # pass




class StartButton():

    def __init__(self, menu):
        self.game = menu.game
        self.menu = menu
        self.width = math.floor(menu.width * .35)
        self.height = math.floor(menu.height * .50)
        self.x = self.menu.x + math.floor(0.1 * self.menu.width)
        self.y = self.menu.y + math.floor(0.1 * self.menu.height)


    def render(self):
        pygame.draw.rect(self.game.screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
        textsurface = myfont.render('Start', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x,self.y))

    def handle_mouse_down(self, x, y):
        if ( x <= self.x + self.width and x >= self.x and
            y <= self.y + self.height and y >= self.y):
            self.game.round.start()
            # tower = Tower(self.game, x, y)
            # tower.dragging = True
            # self.selected_tower = tower
            # self.game.map.towers.append(tower)
            #  print('tower?')
# class TowerIcon():
    
#     def __init__(self, tower_select):
#         self.game = tower_select.game
#         self.tower_select = tower_select
#         self.width = math.floor(tower_select.width * .10)
#         self.height = math.floor(tower_select.height * .50)
#         self.x = self.tower_select.x + math.floor(0.1 * self.tower_select.width)
#         self.y = self.tower_select.y + math.floor(0.1 * self.tower_select.height)
#         self.selected_tower = None
#         pass


#     def render(self):
#         pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
    
#     def handle_mouse_down(self, x, y):
#         if ( x <= self.x + self.width and x >= self.x and
#              y <= self.y + self.height and y >= self.y):
#              tower = Tower(self.game, x, y)
#              tower.dragging = True
#              self.selected_tower = tower
#              self.game.map.towers.append(tower)
#             #  print('tower?')
    
#     # def handle_mouse_up(self, x, y):
#     #     pass

#     def handle_mouse_up(self, x, y):
#         # self.x, self.y = x, y
#         if (self.selected_tower):
#             self.selected_tower.x, self.selected_tower.y = x, y
#             self.selected_tower.dragging = False
#             self.selected_tower = None
             


    
