import pygame
from Player import Player


class Controller:
    # example of player movement
    p1 = Player(50, 50, "green")
    print(p1.pos)
    p1.move("left")
    print(p1.pos)
