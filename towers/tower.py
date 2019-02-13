
import pygame
import math

class Tower():

    def __init__(self, game, x, y):
        self.map = game.map
        self.game = game
        self.dragging = False
        self.attack_wait = 0
        self.x = x
        self.y = y
        self.map.towers.append(self)
        self.targeted_enemy = None
        self.fired_projectiles = []

        # Attributes
        self.range = 200
        self.attack_speed = 100
        self.width = 20
        self.height = 50
        self.attack = 25

    def render(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        for projectile in self.fired_projectiles:
            projectile.render()
    
    def fire_projectile(self):
        projectile = Projectile(self)
        self.fired_projectiles.append(projectile)
        self.attack_wait = self.attack_speed
        projectile.fire()

    def try_attack(self):
        if (self.dragging):
            return
        if (self.attack_wait != 0):
            self.attack_wait -= 1
            return
        # No enemy in target, check for new target
        if (not self.targeted_enemy):
            for enemy in self.map.current_round.enemies:
                dist = math.sqrt(pow(self.x - enemy.x, 2) + pow(self.y - enemy.y, 2))
                # Check if enenmy is in range
                if (dist <= self.range):
                    self.targeted_enemy = enemy
                    self.fire_projectile()
                    break
        # Already has a target
        else:
            dist = math.sqrt(pow(self.x - self.targeted_enemy.x, 2) + pow(self.y - self.targeted_enemy.y, 2))
            # Check if still in range
            if (dist >= self.range):
                self.targeted_enemy = None
            else:
                self.fire_projectile()

    def handle_mouse_down(self, x, y):
        if (x >= self.x and x <= (self.x + self.width)  and
            y >= self.y and y <= (self.y + self.height) and 
            not self.dragging):
            self.map.selected_tower = self

    def handle_mouse_up(self, x, y):
        pass



    def handle_mouse_motion(self, x, y):
        if (self.dragging):
            self.x, self.y = x, y





class Projectile():

    def __init__(self, tower):
        self.tower = tower
        self.game = tower.game
        self.targeted_enemy = tower.targeted_enemy
        self.x, self.y = tower.x, tower.y
        self.slope = abs((self.y - self.targeted_enemy.y) / (self.x - self.targeted_enemy.x))
        self.flying = False
        self.width = 5
        self.height = 5
        self.speed = 7
        self.targeted_enemy_x, self.targeted_enemy_y = tower.targeted_enemy.x, tower.targeted_enemy.y

    def fire(self):
        self.flying = True

    def render(self):
        # print(self.slope)
        # future_30_x = self.x + 30 if self.x <= self.targeted_enemy_x else self.x - 30
        # future_30_y = self.x + (30 * self.slope) if self.x <= self.targeted_enemy_y else self.x - (30 * self.slope)
        # print(f'in 30 clocks u will be at  {future_30_x, future_30_y}')
        if (self.flying):
            # print(f'{self.x, self.y}')
            # print(f'{self.targeted_enemy_x, self.targeted_enemy_y}')
            # if (self.x == self.targeted_enemy_x and
        
            if (self.x <= self.targeted_enemy_x):
                self.x += (1 * self.speed)
                print(f'{self.x, self.y}')

            elif (self.x >= self.targeted_enemy_x):
                self.x -= (1 * self.speed)
                print(f'{self.x, self.y}')

            if (self.y <= self.targeted_enemy_y):
                self.y += (self.speed * self.slope)
                print(f'{self.x, self.y}')

            elif (self.y >= self.targeted_enemy_y):
                self.y -= (self.speed * self.slope)
                print(f'{self.x, self.y}')

            if ( -self.targeted_enemy.height < self.y - self.targeted_enemy_y < self.targeted_enemy.height and
                -self.targeted_enemy.width < self.x - self.targeted_enemy_x < self.targeted_enemy.height):
                self.flying = False
                self.targeted_enemy.hp -= self.tower.attack
                print(self.targeted_enemy.hp)

            # else:
            #     # self.y == self.targeted_enemy_y):
            #     self.flying = False
            #     self.targeted_enemy.hp -= self.tower.attack
            #     print(self.targeted_enemy.hp)

            # print(f'{self.x, self.y}')
            # print(f'{self.targeted_enemy_x, self.targeted_enemy_y}')
            # point_list = [(self.x, self.y), (self.targeted_enemy.x, self.targeted_enemy.y), (self.x, self.targeted_enemy.y)]
            # pygame.draw.polygon(self.game.screen, (0, 0, 255), point_list, 3)
            pygame.draw.rect(self.game.screen, (0, 0, 255), (self.x, self.y, self.width, self.height))






