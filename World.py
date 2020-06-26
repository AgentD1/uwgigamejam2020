import pygame


class World:
    def __init__(self, background_width, background_height, world_width, world_height, tiles):
        self.world_width = world_width
        self.world_height = world_height
        self.tiles = tiles
        self.background = pygame.Surface((background_width, background_height))
