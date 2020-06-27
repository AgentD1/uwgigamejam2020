import pygame

from Tile import Tile
from tiletype import TileType


class Battery():
    def __init__(self, x, y, world, main, on, tilesAttachedTo, upperLimit, lowerLimit):
        self.tiles_attached_to = tilesAttachedTo
        self.main = main
        self.on = on
        self.lower_limit = lowerLimit
        self.upper_limit = upperLimit
        self.world = world
        self.x = x
        self.y = y
    
    def rotate(self, amount):
        if amount == 0:
            return
        tile: Tile
        new_tiles_to_add = []
        for tile in self.tiles_attached_to:
            direction_x = tile.tx - self.x
            direction_y = tile.ty - self.y
            if direction_x == direction_y == 0:
                continue
            if amount < 0:  # counter clockwise
                new_x = -direction_y + self.x
                new_y = direction_x + self.y
                new_tile_type = self.world.tile_rotated_relative(tile.tile_type.name, True)
            else:  # clockwise
                new_x = direction_y + self.x
                new_y = -direction_x + self.y
                new_tile_type = self.world.tile_rotated_relative(tile.tile_type.name, False)
            
            new_tiles_to_add.append(Tile(new_x * 50, new_y * 50, self.world.tile_type_dict[new_tile_type], tile.world_surface))
        
        self.tiles_attached_to = new_tiles_to_add
        
        for tile in new_tiles_to_add:
            self.world.tiles[tile.tx][tile.ty] = tile
