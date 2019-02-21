import pygame, math

icon = pygame.transform.scale( pygame.image.load("images/kobold.png"), (20, 20))

class Enemy():

    def __init__(self, rround):
        self.x = 0
        self.y = 0
        self.round = rround
        self.game = rround.game
        self.map = rround.map
        self.current_tile = None
        self.attack = 1

        # Default Attributes
        self.width = 20
        self.height = 20
        self.max_speed = 3
        self.speed = self.max_speed
        self.is_alive = False
        self.attack = 2
        self.max_hp = 50
        self.hp = self.max_hp
        self.bounty = 1
        self.icon = icon

    def die(self):
        self.is_alive = False
        try:
            self.round.enemies.remove(self)
        except:
            print('failed to delete')
            pass



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
            self.game.screen.blit(self.icon, (self.x, self.y))

            # pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
