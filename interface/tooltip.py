from .interface import Interface
from settings import tooltip_width, tooltip_height, tooltip_x ,tooltip_icon, tooltip_margin
import environment
import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)



class ToolTip(Interface):

    def __init__(self, map_, y, text):
        Interface.__init__(self, map_, tooltip_x, y, tooltip_width, tooltip_height, tooltip_icon)
        self.screen = environment.Game.screen
        self.text = text
        # self.width = math.floor(tower_select.width * .90)
        # self.height = math.floor(tower_select.height * .1)
        # self.icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (self.width, self.height))

    def render(self):
        # self.x = x
        # self.y = y
        self.screen.blit(self.icon, (self.x, self.y))
        # textsurface = myfont.render(f'{self.text}', False, (0, 0, 0))
        # self.screen.blit(textsurface,(self.x + tooltip_margin, (self.y + tooltip_margin)))
        pos = (self.x + tooltip_margin, (self.y + tooltip_margin))
        self.blit_text(pos)
        # pygame.transform.scale(self.icon, (self.width, self.height))

    def handle_mouse_down(self, x, y):
        self.map.tower_select.tooltip = None

        # if ( x <= self.x + self.width and x >= self.x and
        #     y <= self.y + self.height and y >= self.y and
        #     not self.map.round.is_started):
        #     self.map.round.start()

    def blit_text(self, pos, color=pygame.Color('black')):
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
        space = myfont.size(' ')[0]  # The width of a space.
        max_width, max_height = self.screen.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = myfont.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.