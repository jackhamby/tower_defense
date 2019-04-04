from .interface import Interface
from settings import tooltip_width, tooltip_height, tooltip_icon
import environment

class ToolTip(Interface):

    def __init__(self, map_, x, y):
        Interface.__init__(self, map_, x, y, tooltip_width, tooltip_height, tooltip_icon)
        self.screen = environment.Game.screen
        # self.width = math.floor(tower_select.width * .90)
        # self.height = math.floor(tower_select.height * .1)
        # self.icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (self.width, self.height))

    def render(self):
        print('rendering')
        # self.x = x
        # self.y = y
        # pygame.transform.scale(self.icon, (self.width, self.height))
        self.screen.blit(self.icon, (self.x, self.y))

    def handle_mouse_down(self, x, y):
        pass
        # if ( x <= self.x + self.width and x >= self.x and
        #     y <= self.y + self.height and y >= self.y and
        #     not self.map.round.is_started):
        #     self.map.round.start()

