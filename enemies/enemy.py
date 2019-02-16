import pygame, math


class Enemy():

    def __init__(self, rround):
        self.x = -1
        self.y = -1
        self.round = rround
        self.game = rround.game
        self.map = rround.map
        self.current_tile = None

    def die(self):
        self.is_alive = False
        for i, enemy in enumerate(self.round.enemies):
            if (enemy == self):
                # print('deleting')
                del self.round.enemies[i]

    def spawn(self):
        self.is_alive = True
        self.current_tile = self.map.map[7][4]
        self.x = self.map.map[7][4].x + math.floor(self.map.map[7][4].width/2)
        self.y = self.map.map[7][4].y + self.map.map[7][4].height

    def render(self):
        self.y -= self.speed
        tile = self.map.get_tile(self.x, self.y)
        if (tile):
            self.current_tile = tile
        if (self.is_alive):
            pygame.draw.rect(self.game.screen, (0, 255, 0), (self.x, self.y - 10, self.width * (self.hp/self.max_hp), 5))
            pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
