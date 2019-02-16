import pygame
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

class PlayerDisplay():

    def __init__(self, game):
        self.game = game
        self.width = math.floor(SCREEN_WIDTH * 0.25)
        self.height = math.floor(SCREEN_HEIGHT * 0.25)
        self.display_attributes = ["health", "gold"]
        self.margin = 25
        self.text_margin = 5
        self.x = SCREEN_WIDTH - self.width
        self.y = self.margin

        # self.buttons = [StartButton(self)]


    def render(self):
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y, self.width - self.margin, self.height))

        # Show heatlh
        textsurface = myfont.render(f'health {self.game.player.health}', False, (255, 255, 255))
        self.game.screen.blit(textsurface,(self.x + self.text_margin,self.y + self.text_margin))

        # Show gold
        textsurface = myfont.render(f'gold {self.game.player.gold}', False, (255, 255, 255))
        self.game.screen.blit(textsurface,(self.x + self.text_margin, self.y + (self.text_margin * 6)))



    def handle_mouse_down(self, x, y):
        pass


    def handle_mouse_up(self, x, y):
        pass
