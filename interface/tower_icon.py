import environment
from .tooltip import ToolTip
from .interface import Interface
from settings import tower_icon_height, tower_icon_width, locked_icon, in_development_mode
import pygame, math

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


class TowerIcon(Interface):
    ''' Tower icon for purchasing towers in the TowerSelect class '''
    # width = tower_icon_width
    # height = tower_icon_height
    
    def __init__(self, map_, tower, x, y):
        self.tower = tower
        Interface.__init__(self, map_, x, y, tower_icon_width, tower_icon_height, self.tower.icon)
        self.screen = environment.Game.screen
        self.selected_tower = None

    @property 
    def is_unlocked(self):
        return self.tower.unlock_level <= self.map.round.level



    def render(self):
        # self.x = x
        # self.y = y

        margin = math.floor(self.height * .05)
        rect_width = self.tower.width + math.floor(self.tower.width * 0.7)
        rect_height = self.tower.height + math.floor(self.tower.height * 0.25)
        price_width = rect_width
        price_height = math.floor(rect_height * .35)
        tower_x = self.x + math.floor(rect_width/2) - math.floor(self.tower.width/2)
        tower_y = self.y + math.floor(rect_height/2) - math.floor(self.tower.height/2)

        if (self.tower.unlock_level > self.map.round.level and not in_development_mode):
            locked_icon = pygame.transform.scale( pygame.image.load("images/locked_icon.png"), (rect_width, rect_height))
            self.screen.blit(locked_icon, (self.x, self.y))
            return 


        # Draw dithered background
        s = pygame.Surface((rect_width, rect_height))
        s.set_alpha(128)
        s.fill((10, 10, 10))
        self.screen.blit(s, (self.x, self.y))

        # Draw dithered background and price
        s2 = pygame.Surface((price_width, price_height))
        s2.set_alpha(128)
        s2.fill((10, 10, 10))
        self.screen.blit(s2, (self.x, self.y + rect_height + margin))
        textsurface = myfont.render(f'${self.tower.price}', False, (0, 0, 0))
        self.screen.blit(textsurface,(self.x, (self.y + rect_height)))


        # Draw tower icon
        self.screen.blit(self.tower.icon, (tower_x, tower_y))


    def handle_mouse_down(self, x, y):

        if (not self.is_unlocked and not in_development_mode):
            return False
        
        if (self.selected_tower):
            current_tile = self.map.get_tile(x, y)
            right_tile = self.map.get_tile(x + self.selected_tower.width, y)
            below_tile = self.map.get_tile(x, y + self.selected_tower.height)

            # Make sure tower doesnt touch path tile
            if (type(current_tile) == environment.PathTile or
                type(right_tile) == environment.PathTile or 
                type(below_tile) == environment.PathTile):
                return
            # Make sure tower isn't behind tower_select
            if (self.selected_tower.x >= self.map.tower_select.x or
                self.selected_tower.y >= self.map.tower_detail.y):
                return 
            self.selected_tower.x, self.selected_tower.y = x, y
            self.selected_tower.is_dragging = False
            # self.selected_tower.init_effects()
            self.selected_tower = None
        elif ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y):
            #  print('clicked!')
             if (environment.Game.player.purchase(self.tower.price)):
                # print('pruchased')
                tower = self.tower(self.map, x, y)
                tower.is_dragging = True
                self.selected_tower = tower
                self.map.towers.append(tower)

    def handle_mouse_motion(self, x, y):
        if ( x <= self.x + self.width and x >= self.x and
             y <= self.y + self.height and y >= self.y and
             self.is_unlocked):
             tooltip = ToolTip(self.map, self.y, self.tower.description)
             self.map.tower_select.tooltip = tooltip
        elif(self.map.tower_select.tooltip and
             self.map.tower_select.tooltip.text == self.tower.description):
            self.map.tower_select.tooltip = None

        




    # def handle_mouse_up(self, x, y):
    #     if (self.selected_tower):
 
             

