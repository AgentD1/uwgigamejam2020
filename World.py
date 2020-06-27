import pygame


class World:
    def __init__(self, background_width, background_height, world_width, world_height, tiles):
        self.world_width = world_width
        self.world_height = world_height
        self.tiles = tiles
        self.background = pygame.Surface((background_width, background_height))
    
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
