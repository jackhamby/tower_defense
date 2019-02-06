import pygame


class Enemy():

    def __init__(self, game):
        self.x = -1
        self.y = -1
        self.game = game
        self.width = 5
        self.height = 5
        self.map = game.map
        self.is_alive = False

    def spawn(self):
        self.is_alive = True
        self.x = self.map.map[7][4].x
        self.y = self.map.map[7][4].y

    def render(self):
        if (self.is_alive):
            pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
