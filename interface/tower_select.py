import pygame, math
from towers import ArrowTower, MagicTower, BombTower, SlimeTower, FireTower, FruitFarm, BoostTower, Tower
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
        self.available_towers = [ArrowTower, MagicTower, BombTower, SlimeTower, FireTower, FruitFarm, BoostTower]

        # Main models to render
        self.data_displays = []
        self.tower_icons = []
        self.go_button = None
        self.tooltip = None

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
            # if (tower_icon.tower.unlock_level > self.map.round.level):
            #     tower_icon.render(is_unlocked=False)
            # else:
            #     tower_icon.render()

        if (self.tooltip):
            self.tooltip.render()
        self.go_button.render()


    def handle_mouse_down(self, x, y):
        # print(len(self.tower_icons))
        for icon in self.tower_icons:
            icon.handle_mouse_down(x, y)
        if (self.tooltip):
            self.tooltip.handle_mouse_down(x, y)
        self.go_button.handle_mouse_down(x, y)

    def handle_mouse_motion(self, x, y):
        for icon in self.tower_icons:
            icon.handle_mouse_motion(x, y)

        