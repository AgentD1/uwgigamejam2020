import pygame
from tiletype import TileType


class Tile:
    def __init__(self, x, y, tile_type: TileType, world_surface: pygame.Surface):
        self.x = x
        self.y = y
        self.tile_type = tile_type
        self.world_surface = world_surface
    
    def draw(self):
        if self.tile_type.anim is None:
            self.world_surface.blit(self.tile_type.sprite, (self.x, self.y))
        else:
            self.world_surface.blit(self.tile_type.anim.current_image, (self.x, self.y))
