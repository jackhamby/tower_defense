import pygame, math
from environment.tile import PathTile, GroundTile
import environment

icon = pygame.transform.scale( pygame.image.load("images/kobold.png"), (20, 20))

class Enemy():

    def __init__(self, map_, width, height, icon):
        self.y_dir = 0
        self.x_dir = 0
        self.width = width
        self.height = height
        self.map = map_
        self.current_tile = None
        self.previous_tile = None
        
        # Default Attributes

        self.max_speed = 5
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 50
        self.hp = self.max_hp
        self.bounty = 1
        self.icon = icon

    def die(self):
        if (not self.is_alive):
            return
        self.is_alive = False
        # print(self.map.enemies)
        try:
            self.map.enemies.remove(self)
        except:
            print('failed to delete')
            pass

    def take_damage(self, damage):
            self.hp -= damage
            if (self.hp <= 0):
                self.die()
                environment.Game.player.gold += self.bounty
                # self.fired_projectiles.remove(projectile)


    def attack(self):
        environment.Game.player.health -= self.damage



    def spawn(self):
        self.current_tile = self.map.starting_tile
        self.x = self.current_tile.x + math.floor(self.current_tile.width / 2) - math.floor(self.width / 2)
        self.y = self.current_tile.y + self.current_tile.height - math.floor(self.height / 2)
        self.is_alive = True
        print('spawned')


    def follow_path(self):
        # Check all adjacent tiles
        # print(f'im at {self.current_tile.x_index}, {self.current_tile.y_index}')
        x_index = self.current_tile.x_index
        y_index = self.current_tile.y_index

        if (self.current_tile.is_end):
            self.update_board((self.x_dir, self.y_dir))
            return 

        # Check tile below
        if (y_index + 1 < self.map.height):                
            tile = self.map.tiles[y_index + 1][x_index]
            if (type(tile) == PathTile 
                and tile != self.previous_tile):
                self.update_board((0, 1))
                return

        # Check above 
        if (y_index - 1 >= 0): 
            tile = self.map.tiles[y_index - 1][x_index]
            if (type(tile) == PathTile and
                tile != self.previous_tile):
                self.update_board((0, -1))
                return 

        # Check left
        if  (x_index - 1 >= 0):
            tile = self.map.tiles[y_index][x_index - 1]
            if (type(tile) == PathTile 
                and tile != self.previous_tile):
                self.update_board((-1, 0))
                return 

        # Check right
        if  (x_index + 1 < self.map.width):
            tile = self.map.tiles[y_index][x_index + 1]
            if (type(tile) == PathTile 
                and tile != self.previous_tile):
                self.update_board((1, 0))
                return



    def update_board(self, direction):
        x_dir = direction[0]
        y_dir = direction[1]
        current_tile = self.map.get_tile(self.x, self.y)
        if (not current_tile):
            self.attack()
            self.die()
            return
        tile_center_x = current_tile.x + math.floor(current_tile.width / 2)
        tile_center_y = current_tile.y + math.floor(current_tile.height / 2)
        enemy_center_x = self.x + math.floor(self.width / 2)
        enemy_center_y = self.y + math.floor(self.height / 2)
        is_in_center =  self.check_in_center((enemy_center_x, enemy_center_y), (tile_center_x, tile_center_y))
        if ( ((x_dir != self.x_dir or y_dir != self.y_dir) and is_in_center) or
            (self.x_dir == 0 and self.y_dir ==0)):
            self.x_dir = x_dir
            self.y_dir = y_dir
        self.x += self.x_dir * (self.speed) 
        self.y += self.y_dir * (self.speed)
        if (current_tile != self.current_tile):
            self.previous_tile = self.current_tile
            self.current_tile = current_tile
            

    def check_in_center(self, enemy_center_pos, tile_center_pos):
        enemy_center_x = enemy_center_pos[0]
        enemy_center_y = enemy_center_pos[1]
        tile_center_x = tile_center_pos[0]
        tile_center_y = tile_center_pos[1]
        margin = math.floor(self.current_tile.width / 10)    # Margin for 'in center'
        if (enemy_center_x <= (tile_center_x + margin) and 
            enemy_center_x >= (tile_center_x - margin) and
            enemy_center_y <= (tile_center_y + margin) and
            enemy_center_y >= (tile_center_y - margin)):
            return True
        return False


    def render(self):
        if (not self.is_alive):
            return
        self.follow_path()
        if (self.is_alive):
            pygame.draw.rect(environment.Game.screen, (0, 255, 0), (self.x, self.y - 10, self.width * (self.hp/self.max_hp), 5))
            environment.Game.screen.blit(self.icon, (self.x, self.y))