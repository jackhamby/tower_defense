import pygame, math
from towers import ArrowTower, MagicTower, Tower
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)



class TowerSelect():
    width = math.floor(SCREEN_WIDTH * 0.15)
    height = SCREEN_HEIGHT
    icon = pygame.transform.scale( pygame.image.load("images/woodwall.png"), (width, height))
    x = SCREEN_WIDTH - width
    y = 0


    def __init__(self, game):
        self.game = game
        # self.x = 0 
        # self.y = SCREEN_HEIGHT - self.height
        self.data_displays = [DataDisplay(self, "gold"), DataDisplay(self, "health")]
        self.tower_icons = [TowerIcon(self, ArrowTower), TowerIcon(self, MagicTower)]
        self.go_button = GoButton(self)


    def render(self):
        # textsurface = myfont.render(f'Shop', False, (0, 0, 0))
        # self.game.screen.blit(textsurface,(self.x, self.y - (self.text_margin * 6)))

        # Render main block
        self.game.screen.blit(self.icon, (self.x, self.y))

        # pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        margin = math.floor(SCREEN_WIDTH * .01)


        # Render data displays
        x = self.x + margin
        y = self.y + margin
        for display in self.data_displays:
            display.render(x, y)
            y += (display.height + margin)

        # Render icons in rows of 2
        # Start rendering icons 1/5 down page
        x = self.x + margin
        y = y + margin
        count = 0
        for icon in self.tower_icons:
            icon.render(x, y)
            x += (icon.width + margin)
            count += 1
            if (count % 2 == 0):
                y += (icon.height + margin)

        
        # Render go button
        x = self.x + margin
        y = y + margin
        self.go_button.render(x, y)
        


    def handle_mouse_down(self, x, y):
        for icon in self.tower_icons:
            icon.handle_mouse_down(x, y)
        self.go_button.handle_mouse_down(x, y)


    def handle_mouse_up(self, x, y):
        for icon in self.tower_icons:
            icon.handle_mouse_up(x, y)
        # pass




class GoButton():

    def __init__(self, tower_select):
        self.tower_select = tower_select
        self.game = tower_select.game
        self.width = math.floor(tower_select.width * .90)
        self.height = math.floor(tower_select.height * .1)
        self.icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (self.width, self.height))

    def render(self, x, y):
        self.x = x
        self.y = y
        # pygame.transform.scale(self.icon, (self.width, self.height))
        self.game.screen.blit(self.icon, (self.x, self.y))

    def handle_mouse_down(self, x, y):
        if ( x <= self.x + self.width and x >= self.x and
            y <= self.y + self.height and y >= self.y):
            self.game.round.start()



class DataDisplay():


    def __init__(self, tower_select, attribute_name):
        self.tower_select = tower_select
        self.game = tower_select.game
        self.attribute = attribute_name
        self.width = math.floor(tower_select.width * .90)
        self.height = math.floor(tower_select.height * .05)
        self.icon =  pygame.transform.scale( pygame.image.load(f'images/input_{self.attribute}.png'), (self.width, self.height))

    def render(self, x, y):
        self.x = x
        self.y = y
        # pygame.transform.scale(self.icon, (self.width, self.height))
        self.game.screen.blit(self.icon, (self.x, self.y))

        textsurface = myfont.render(f'${getattr(self.game.player, self.attribute)}', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x + math.floor(self.width * .3), self.y + math.floor(self.height * .1)))
    
        # Render data 








class TowerIcon():
    
    def __init__(self, tower_select, tower):
        self.tower = tower
        self.game = tower_select.game
        self.tower_select = tower_select
        self.width = math.floor(tower_select.width * .50)
        self.height = math.floor(tower_select.height * .10)
        # self.x = self.tower_select.x + math.floor(0.1 * self.tower_select.width)
        # self.y = self.tower_select.y + math.floor(0.1 * self.tower_select.height)
        self.selected_tower = None


    def render(self, x, y):
        self.x = x
        self.y = y
        margin = math.floor(self.height * .05)
        rect_width = self.tower.width + math.floor(self.tower.width * 0.7)
        rect_height = self.tower.height + math.floor(self.tower.height * 0.25)
        price_width = rect_width
        price_height = math.floor(rect_height * .3)
        tower_x = self.x + math.floor(rect_width/2) - math.floor(self.tower.width/2)
        tower_y = self.y + math.floor(rect_height/2) - math.floor(self.tower.height/2)

        # Draw dithered background
        s = pygame.Surface((rect_width, rect_height))
        s.set_alpha(128)
        s.fill((10, 10, 10))
        self.game.screen.blit(s, (self.x, self.y))

        # Draw dithered background and price
        s2 = pygame.Surface((price_width, price_height))
        s2.set_alpha(128)
        s2.fill((10, 10, 10))
        self.game.screen.blit(s2, (self.x, self.y + rect_height + margin))
        textsurface = myfont.render(f'${self.tower.price}', False, (0, 0, 0))
        self.game.screen.blit(textsurface,(self.x, (self.y + rect_height)))


        # Draw tower icon
        self.game.screen.blit(self.tower.icon, (tower_x, tower_y))

        # self.game.screen.blit(self.tower.icon, (self.x + math.floor(rect_width/4), self.y ))

        # textsurface = myfont.render(f'${self.tower.price}', False, (0, 0, 0))
        # self.game.screen.blit(textsurface,(self.x, (self.y + self.height) + self.tower_select.text_margin))
    
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
             


    
