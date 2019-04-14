from .interface import Interface
from settings import sell_button_width, sell_button_height,  sell_button_x, sell_button_y, sell_button_icon 
import environment
import math

class SellButton(Interface):

    def __init__(self, map_, tower):
        Interface.__init__(self, map_, sell_button_x, sell_button_y, sell_button_width, sell_button_height, sell_button_icon)
        self.screen = environment.Game.screen
        self.tower = tower
        # self.width = math.floor(tower_select.width * .90)
        # self.height = math.floor(tower_select.height * .1)
        # self.icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (self.width, self.height))

    def render(self):
        # self.x = x
        # self.y = y
        # pygame.transform.scale(self.icon, (self.width, self.height))
        self.screen.blit(self.icon, (self.x, self.y))

    def handle_mouse_down(self, x, y):
        # print('handling mouse down on sell')
        if ( x <= self.x + self.width and x >= self.x and
            y <= self.y + self.height and y >= self.y):
            # self.map.round.start()
            environment.Game.player.sell(math.floor(self.tower.price / 2))
            self.tower.remove()
            self.map.selected_tower = None


