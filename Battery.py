from Tile import Tile

main_battery = (0, 0)


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
        print(len(self.tiles_attached_to))
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
        else:
            self.current_rotation = clockwiseMoves[self.current_rotation]
        tile: Tile
        new_tiles_to_add = []
        for tile in self.tiles_attached_to:
            old_pos_x = tile.tx
            old_pos_y = tile.ty
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
            self.world.tiles[old_pos_x][old_pos_y] = Tile(old_pos_x * 50, old_pos_y * 50, self.world.tile_type_dict[""], tile.world_surface)
            new_tiles_to_add.append(Tile(new_x * 50, new_y * 50, self.world.tile_type_dict[new_tile_type], tile.world_surface))
        
        self.tiles_attached_to = new_tiles_to_add
        
        for tile in new_tiles_to_add:
            self.world.tiles[tile.tx][tile.ty] = tile
    
    def set_this_to_main_battery(self):
        if not self.main:
            self.set_main_battery(self.x, self.y)
    
    def set_main_battery(self, x, y):
        global main_battery
        if main_battery != (0, 0):
            self.world.tiles[main_battery[0]][main_battery[1]].tile_type = self.world.tile_type_dict["batteryNotMain"]
            for battery in self.world.batteries:
                if battery.x == main_battery[0] and battery.y == main_battery[1]:
                    battery.main = False
                    break
        
        main_battery = (x, y)
        self.world.tiles[main_battery[0]][main_battery[1]].tile_type = self.world.tile_type_dict["batteryMain"]
        for battery in self.world.batteries:
            if battery.x == main_battery[0] and battery.y == main_battery[1]:
                battery.main = True
                break
