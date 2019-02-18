
import pygame
import math

class Tower():

    def __init__(self, game, x, y):
        self.map = game.map
        self.game = game
        self.level = 1
        self.dragging = False
        self.attack_wait = 0
        self.x = x
        self.y = y
        # self.map.towers.append(self)
        self.targeted_enemy = None
        self.fired_projectiles = []
        self.upgrades = []


    def render(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        for projectile in self.fired_projectiles:
            projectile.render()
    
    def fire_projectile(self):
        projectile = Projectile(self)
        self.fired_projectiles.append(projectile)
        self.attack_wait = self.attack_speed
        projectile.fire()
        print(self.fired_projectiles)

    def try_attack(self):
        if (self.dragging):
            return
        if (self.attack_wait != 0):
            self.attack_wait -= 1
            return
        # No enemy in target, check for new target
        if (not self.targeted_enemy):
            for enemy in self.game.round.enemies:
                dist = math.sqrt(pow(self.x - enemy.x, 2) + pow(self.y - enemy.y, 2))
                # Check if enenmy is in range
                if (dist <= self.range):
                    self.targeted_enemy = enemy
                    self.fire_projectile()
                    break
        # Already has a target which is alive
        elif(self.targeted_enemy.is_alive):
            dist = math.sqrt(pow(self.x - self.targeted_enemy.x, 2) + pow(self.y - self.targeted_enemy.y, 2))
            # Check if still in range
            if (dist >= self.range):
                self.targeted_enemy = None
            else:
                self.fire_projectile()

        # Its current target died
        else:
            self.targeted_enemy = None
            return 


    def handle_mouse_down(self, x, y):
        if (x >= self.x and x <= (self.x + self.width)  and
            y >= self.y and y <= (self.y + self.height) and 
            not self.dragging):
            tower_detail = self.game.get_tower_detail()
            if (tower_detail):
                tower_detail.selected_tower = self
                tower_detail.set_upgrade_icons()
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
        self.speed = self.tower.projectile_speed
        self.targeted_enemy_x, self.targeted_enemy_y = tower.targeted_enemy.x, tower.targeted_enemy.y

    def fire(self):
        self.flying = True

    def die(self):
        self.flying = False
        print('dying')
        self.tower.fired_projectiles.remove(self)

        # for i, projectile in enumerate(self.tower.fired_projectiles):
        #     if (projectile == self):
        #         del self.tower.fired_projectiles[i]
        #         print('destroyed projectile')
        #         break

    def render(self):
        if (self.flying):
            if (self.x <= self.targeted_enemy_x):
                self.x += (1 * self.speed)
                

            elif (self.x >= self.targeted_enemy_x):
                self.x -= (1 * self.speed)

            if (self.y <= self.targeted_enemy_y):
                self.y += (self.speed * self.slope)

            elif (self.y >= self.targeted_enemy_y):
                self.y -= (self.speed * self.slope)

            if ( -self.targeted_enemy.height < self.y - self.targeted_enemy_y < self.targeted_enemy.height and
                -self.targeted_enemy.width < self.x - self.targeted_enemy_x < self.targeted_enemy.height):
                self.targeted_enemy.hp -= self.tower.attack
                if (self.targeted_enemy.hp <= 0):
                    self.tower.targeted_enemy = None
                    self.game.player.gold += self.targeted_enemy.bounty
                    self.targeted_enemy.die()
                self.die()
 
            pygame.draw.rect(self.game.screen, (0, 0, 255), (self.x, self.y, self.width, self.height))






