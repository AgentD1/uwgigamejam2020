from Tile import Tile


class Battery:
    def __init__(self, x, y, world, main, on, tilesAttachedTo, upperLimit, lowerLimit):
        self.tiles_attached_to = tilesAttachedTo
        self.main = main
        self.on = on
        self.lower_limit = lowerLimit
        self.upper_limit = upperLimit
        self.world = world
        self.x = x
        self.y = y
        self.current_rotation = "up"
    
    def rotate(self, amount):
        if amount == 0:
            return
        clockwiseMoves = {"left": "up",
                          "up": "right",
                          "right": "down",
                          "down": "left"}
        counterClockwiseMoves = {v: k for k, v in clockwiseMoves.items()}
        if amount < 0 and self.current_rotation == self.upper_limit:
            return
        if amount > 0 and self.current_rotation == self.lower_limit:
            return
        if amount < 0:
            self.current_rotation = counterClockwiseMoves[self.current_rotation]
            print(self.current_rotation)
        else:
            self.current_rotation = clockwiseMoves[self.current_rotation]
            print(self.current_rotation)
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
