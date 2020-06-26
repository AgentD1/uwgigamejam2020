import pygame


class World:
    def __init__(self, width, height, tiles, board):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.board = board
