from .interface import Interface
from settings import tower_detail_display_width, tower_detail_display_height, tower_detail_display_x, tower_detail_display_y, tower_detail_display_icon 
import environment
import math
import pygame

# Set fonts
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


class TowerDetailDisplay(Interface):

    def __init__(self, map_, tower):
        Interface.__init__(self, map_, tower_detail_display_x, tower_detail_display_y, tower_detail_display_width, tower_detail_display_height, tower_detail_display_icon)
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
        self.text = f'''  attack: {self.tower.attack}
  speed: {self.tower.attack_speed}
  range: {self.tower.range}
        '''

        self.blit_text((self.x, self.y))
        # textsurface = myfont.render(f'attack: {self.tower.attack}', False, (0, 0, 0))
        # text_x = self.x + math.floor(self.width * .1)
        # text_y = self.y + math.floor(self.height * .01)
        # environment.Game.screen.blit(textsurface,(text_x, text_y))


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


