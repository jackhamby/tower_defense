import pygame, math


class Enemy():

    def __init__(self, rround):
        self.x = 0
        self.y = 0
        self.round = rround
        self.game = rround.game
        self.map = rround.map
        self.current_tile = None
        self.attack = 1

    def die(self):
        self.is_alive = False
        try:
            self.round.enemies.remove(self)
        except:
            # print(self.round.enemies)
            print('failed to delete')
            pass

        # print(self.round.enemies)
        # for i, enemy in enumerate(self.round.enemies):
        #     if (enemy == self):
        #         # print('deleting')
        #         del self.round.enemies[i]
        #         # print(len(self.round.enemies))


    def spawn(self):
        self.is_alive = True
        self.current_tile = self.map.map[7][4]
        self.x = self.map.map[7][4].x + math.floor(self.map.map[7][4].width/2)
        self.y = self.map.map[7][4].y + self.map.map[7][4].height

    def render(self):
        if (not self.is_alive):
            return
        self.y -= self.speed
        tile = self.map.get_tile(self.x, self.y)
        # print(self.y)
        if ((self.y + self.height) < 0):
            # print('die')
            self.die()
            self.game.player.health -= self.attack
            # print(len(self.round.enemies))
        if (tile):
            self.current_tile = tile
        if (self.is_alive):
            pygame.draw.rect(self.game.screen, (0, 255, 0), (self.x, self.y - 10, self.width * (self.hp/self.max_hp), 5))
            pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
