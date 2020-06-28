import pygame

from Tile import Tile


class World:
    def __init__(self, background_width, background_height, world_width, world_height, tiles, tile_type_dict):
        self.world_width = world_width
        self.world_height = world_height
        self.tiles = tiles
        self.background = pygame.Surface((background_width, background_height))
        self.tile_type_dict = tile_type_dict
        self.batteries = None
    
    def tile_rotated_absolute(self, tile, rotation_direction):
        if tile in ["batteryMain", "batteryNotMain", "batteryOff", ""]:
            return tile
        
        tile_append = tile[-1]
        tile = tile[0:-1]
        compression = {("ud", "lr"): "hor",
                       ("ul", "ur", "dl", "dr"): "turn",
                       ("ulr", "udl", "udr", "dlr"): "3turn",
                       ("udlr",): "4turn"}
        decompression = {("hor", "left"): "lr",  # Straight tiles
                         ("hor", "right"): "lr",
                         ("hor", "up"): "ud",
                         ("hor", "down"): "ud",
                         ("turn", "left"): "dl",  # Turn tiles
                         ("turn", "right"): "ur",
                         ("turn", "up"): "ul",
                         ("turn", "down"): "dr",
                         ("3turn", "left"): "udl",  # 3Turn tiles
                         ("3turn", "right"): "udr",
                         ("3turn", "up"): "ulr",
                         ("3turn", "down"): "dlr",
                         ("4turn", "down"): "udlr",  # 4Turn tile
                         ("4turn", "left"): "udlr",
                         ("4turn", "up"): "udlr",
                         ("4turn", "right"): "udlr"
                         }
        for (key, value) in compression.items():
            if tile in key:
                return decompression[(value, rotation_direction)] + tile_append
        return "error"
    
    def tile_rotated_relative(self, tile, clockwise):
        if tile in ["batteryMain", "batteryNotMain", "batteryOff", ""]:
            return tile
        clockwiseMoves = {"left": "up",
                          "up": "right",
                          "right": "down",
                          "down": "left"}
        
        tile_direction = self.get_tile_direction(tile)
        
        new_direction = clockwiseMoves[tile_direction]
        
        if not clockwise:
            new_direction = clockwiseMoves[clockwiseMoves[new_direction]]
        
        return self.tile_rotated_absolute(tile, new_direction)
    
    def get_tile_direction(self, tile: str):
        tile = tile[0:-1]
        return {"ud": "up",  # Horizontal tiles
                "lr": "right",
                "ul": "up",  # Turn tiles
                "ur": "right",
                "dr": "down",
                "dl": "left",
                "ulr": "up",  # 3turn tiles
                "udr": "right",
                "dlr": "down",
                "udl": "left",
                "udlr": "up"  # 4turn tiles
                }[tile]
    
    def update_batteries_and_connections(self):
        for row in self.tiles:
            for tile in row:
                if 'p' in tile.tile_type.name:
                    tile.tile_type = self.tile_type_dict[tile.tile_type.name[0:-1] + 'n']
                elif tile.tile_type.name == "batteryNotMain":
                    tile.tile_type = self.tile_type_dict["batteryOff"]
                    for battery in self.batteries:
                        if battery.x == tile.tx and battery.y == tile.ty:
                            battery.on = False
                            break
        
        for row in self.tiles:
            for tile in row:
                if tile.tile_type.name == "batteryMain":
                    battery_locations = self.find_connected_battery_locations(tile.tx, tile.ty)
                    for (mx, my) in battery_locations:
                        if self.tiles[mx][my].tile_type.name == "batteryMain" or self.tiles[mx][my].tile_type.name == "batteryNotMain":
                            continue
                        if self.tiles[mx][my].tile_type.name == "batteryOff":
                            self.tiles[mx][my] = Tile(mx * 50, my * 50, self.tile_type_dict["batteryNotMain"], tile.world_surface)
                            for battery in self.batteries:
                                if battery.x == mx and battery.y == my:
                                    battery.on = True
                                    print("turning on")
                                    break
                    conductors = self.find_connected_battery_locations_and_conductors(tile.tx, tile.ty)
                    for (mx, my) in conductors:
                        if "battery" in self.tiles[mx][my].tile_type.name:
                            continue
                        if 'n' in self.tiles[mx][my].tile_type.name:
                            self.tiles[mx][my].tile_type = self.tile_type_dict[self.tiles[mx][my].tile_type.name[0:-1] + 'p']
    
    def find_connected_battery_locations(self, x, y):
        checked_tile_locations = []
        self.find_connected_battery_locations_recursive(x, y, checked_tile_locations)
        final_list = []
        for (x, y) in checked_tile_locations:
            if "battery" in self.tiles[x][y].tile_type.name:
                final_list.append((x, y))
        return final_list
    
    def find_connected_battery_locations_and_conductors(self, x, y):
        checked_tile_locations = []
        self.find_connected_battery_locations_recursive(x, y, checked_tile_locations)
        return checked_tile_locations
    
    def find_connected_battery_locations_recursive(self, x, y, checked_tile_locations):
        if (x, y) in checked_tile_locations:
            return
        my_tile = self.tiles[x][y]
        checked_tile_locations.append((x, y))
        #       tiles that can conduct power                                other than batteries                             main battery only
        if (('n' in my_tile.tile_type.name or 'p' in my_tile.tile_type.name) and "battery" not in my_tile.tile_type.name) or my_tile.tile_type.name is "batteryMain":
            if "up" in my_tile.tile_type.accessible_to and y - 1 >= 0 and "down" in self.tiles[x][y - 1].tile_type.accessible_from:
                self.find_connected_battery_locations_recursive(x, y - 1, checked_tile_locations)
            if "left" in my_tile.tile_type.accessible_to and x - 1 >= 0 and "right" in self.tiles[x - 1][y].tile_type.accessible_from:
                self.find_connected_battery_locations_recursive(x - 1, y, checked_tile_locations)
            if "right" in my_tile.tile_type.accessible_to and x + 1 < self.world_width and "left" in self.tiles[x + 1][y].tile_type.accessible_from:
                self.find_connected_battery_locations_recursive(x + 1, y, checked_tile_locations)
            if "down" in my_tile.tile_type.accessible_to and y + 1 < self.world_height and "up" in self.tiles[x][y + 1].tile_type.accessible_from:
                self.find_connected_battery_locations_recursive(x, y + 1, checked_tile_locations)
        else:
            return
