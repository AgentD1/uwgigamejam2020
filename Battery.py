import pygame

from Tile import Tile
from tiletype import TileType


class Battery(Tile):
    def __init__(self, x, y, tile_type: TileType, world_surface: pygame.Surface, tilesAttachedTo, rotationDirection, upperLimit, lowerLimit):
        super().__init__(x, y, tile_type, world_surface)
        self.tiles_attached_to = tilesAttachedTo
        self.rotation_direction = rotationDirection
        self.lower_limit = lowerLimit
        self.upper_limit = upperLimit

        