import pygame, math
from towers import ArrowTower, MagicTower, BombTower, SlimeTower, Tower
from .interface import Interface
from .go_button import GoButton
from .data_display import DataDisplay
from .tower_icon import TowerIcon
from settings import tower_select_width, tower_select_height, tower_select_x, tower_select_y, tower_select_icon, tower_select_margin
import environment

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)



class TowerSelect(Interface):

    def __init__(self, _map):
        Interface.__init__(self, _map, tower_select_x, tower_select_y, tower_select_width, tower_select_height, tower_select_icon)
        # self.x = 0 
        
        # self.y = SCREEN_HEIGHT - self.height
        self.screen = environment.Game.screen
        self.available_attributes = ["gold", "health"]
        self.available_towers = [ArrowTower, MagicTower, BombTower, SlimeTower]

        # Main models to render
        self.data_displays = []
        self.tower_icons = []
        self.go_button = None

        # Load player display models
        x, y  = self.x + tower_select_margin, self.y + tower_select_margin
        for attribute in self.available_attributes:
            data_display = DataDisplay(self.map, attribute, x, y)
            self.data_displays.append(data_display)
            y += data_display.height + tower_select_margin

        # Load tower icon models
        x = self.x + tower_select_margin
        y = y + tower_select_margin
        count = 0
        for tower_type in self.available_towers:
            tower_icon = TowerIcon(self.map, tower_type, x, y)
            # print(f'rendering @ {x}, {y}')
            self.tower_icons.append(tower_icon)
            x += (tower_icon.width + tower_select_margin)
            count += 1
            if (count % 2 == 0):
                x = self.x + tower_select_margin
                y += (tower_icon.height + tower_select_margin)
        

        # Load go button model
        x = self.x + tower_select_margin
        y = y + tower_icon.height + tower_select_margin
        self.go_button = GoButton(self.map, x, y)


        # self.data_displays = [DataDisplay("gold"), DataDisplay("health")]
        # self.tower_icons = [TowerIcon(ArrowTower), TowerIcon(MagicTower)]


    def render(self):
        # Render main block
        # print(f'rendering @ {self.x}, {self.y}')
        self.screen.blit(self.icon, (self.x, self.y))

        for data_display in self.data_displays:
            data_display.render()
            
        for tower_icon in self.tower_icons:
            tower_icon.render()

        self.go_button.render()


    def handle_mouse_down(self, x, y):
        # print(len(self.tower_icons))
        for icon in self.tower_icons:
            icon.handle_mouse_down(x, y)
        self.go_button.handle_mouse_down(x, y)


    # def handle_mouse_up(self, x, y):
    #     for icon in self.tower_icons:
    #         icon.handle_mouse_up(x, y)




# class GoButton():

#     def __init__(self, tower_select):
#         self.tower_select = tower_select
#         self.game = tower_select.game
#         self.width = math.floor(tower_select.width * .90)
#         self.height = math.floor(tower_select.height * .1)
#         self.icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (self.width, self.height))

#     def render(self, x, y):
#         self.x = x
#         self.y = y
#         # pygame.transform.scale(self.icon, (self.width, self.height))
#         self.game.screen.blit(self.icon, (self.x, self.y))

#     def handle_mouse_down(self, x, y):
#         if ( x <= self.x + self.width and x >= self.x and
#             y <= self.y + self.height and y >= self.y):
#             self.game.round.start()



# class DataDisplay():


#     def __init__(self, tower_select, attribute_name):
#         self.tower_select = tower_select
#         self.game = tower_select.game
#         self.attribute = attribute_name
#         self.width = math.floor(tower_select.width * .90)
#         self.height = math.floor(tower_select.height * .05)
#         self.icon =  pygame.transform.scale( pygame.image.load(f'images/input_{self.attribute}.png'), (self.width, self.height))

#     def render(self, x, y):
#         self.x = x
#         self.y = y
#         # pygame.transform.scale(self.icon, (self.width, self.height))
#         self.game.screen.blit(self.icon, (self.x, self.y))

#         textsurface = myfont.render(f'${getattr(self.game.player, self.attribute)}', False, (0, 0, 0))
#         self.game.screen.blit(textsurface,(self.x + math.floor(self.width * .3), self.y + math.floor(self.height * .1)))
    
#         # Render data 








# class TowerIcon():
    
#     def __init__(self, tower_select, tower):
#         self.tower = tower
#         self.game = tower_select.game
#         self.tower_select = tower_select
#         self.width = math.floor(tower_select.width * .50)
#         self.height = math.floor(tower_select.height * .10)
#         # self.x = self.tower_select.x + math.floor(0.1 * self.tower_select.width)
#         # self.y = self.tower_select.y + math.floor(0.1 * self.tower_select.height)
#         self.selected_tower = None


#     def render(self, x, y):
#         self.x = x
#         self.y = y
#         margin = math.floor(self.height * .05)
#         rect_width = self.tower.width + math.floor(self.tower.width * 0.7)
#         rect_height = self.tower.height + math.floor(self.tower.height * 0.25)
#         price_width = rect_width
#         price_height = math.floor(rect_height * .35)
#         tower_x = self.x + math.floor(rect_width/2) - math.floor(self.tower.width/2)
#         tower_y = self.y + math.floor(rect_height/2) - math.floor(self.tower.height/2)

#         # Draw dithered background
#         s = pygame.Surface((rect_width, rect_height))
#         s.set_alpha(128)
#         s.fill((10, 10, 10))
#         self.game.screen.blit(s, (self.x, self.y))

#         # Draw dithered background and price
#         s2 = pygame.Surface((price_width, price_height))
#         s2.set_alpha(128)
#         s2.fill((10, 10, 10))
#         self.game.screen.blit(s2, (self.x, self.y + rect_height + margin))
#         textsurface = myfont.render(f'${self.tower.price}', False, (0, 0, 0))
#         self.game.screen.blit(textsurface,(self.x, (self.y + rect_height)))


#         # Draw tower icon
#         self.game.screen.blit(self.tower.icon, (tower_x, tower_y))

#         # self.game.screen.blit(self.tower.icon, (self.x + math.floor(rect_width/4), self.y ))

#         # textsurface = myfont.render(f'${self.tower.price}', False, (0, 0, 0))
#         # self.game.screen.blit(textsurface,(self.x, (self.y + self.height) + self.tower_select.text_margin))
    
#     def handle_mouse_down(self, x, y):
#         if ( x <= self.x + self.width and x >= self.x and
#              y <= self.y + self.height and y >= self.y):
#              if (self.game.player.purchase(self.tower.price)):
#                 # print('creating tower')
#                 tower = self.tower(self.game, x, y)
#                 tower.dragging = True
#                 self.selected_tower = tower
#                 self.game.map.towers.append(tower)
#                 # print(self.game.map.towers)


#     def handle_mouse_up(self, x, y):
#         # self.x, self.y = x, y
#         if (self.selected_tower):
#             self.selected_tower.x, self.selected_tower.y = x, y
#             self.selected_tower.dragging = False
#             self.selected_tower = None
             


    
