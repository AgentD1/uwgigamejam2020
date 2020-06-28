import pygame
import random
from World import World


class Positron:
    def __init__(self, anim, world, x, y):
        self.anim = anim
        self.world = world
        self.x = x
        self.y = y
        self.tx = int(x / 50)
        self.ty = int(y / 50)
    
    def update(self):
        my_tile = self.world.tiles[self.tx][self.ty]
        directions = ["up", "left", "right", "down"]
        random.shuffle(directions)
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        for dire in directions:
            if dire == "up":
                target_tile = self.world.tiles[self.tx][self.ty - 1]
            elif dire == "down":
                target_tile = self.world.tiles[self.tx][self.ty + 1]
            elif dire == "left":
                target_tile = self.world.tiles[self.tx - 1][self.ty]
            else:
                target_tile = self.world.tiles[self.tx + 1][self.ty]
            if dire in my_tile.tile_type.accessible_to and opposites[dire] in target_tile.tile_type.accessible_from:
                self.x = target_tile.x
                self.y = target_tile.y
                self.tx = int(self.x / 50)
                self.ty = int(self.y / 50)
                break
    
    def move(self, tx, ty):
        self.x = tx * 50
        self.y = tx * 50
        self.tx = tx
        self.ty = ty
    
    def draw(self, surf: pygame.Surface):
        surf.blit(self.anim.current_image, (self.x, self.y))
