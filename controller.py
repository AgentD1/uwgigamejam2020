import pygame
from Player import Player


class Controller:
    def __init__(self, p1, camera):
        self.p1 = p1
        self.camera = camera

    def check_keys(self):

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.camera.y += 1
        if keys_pressed[pygame.K_s]:
            self.camera.y -= 1
        if keys_pressed[pygame.K_a]:
            self.camera.x += 1
        if keys_pressed[pygame.K_d]:
            self.camera.x -= 1
        if keys_pressed[pygame.K_j]:
            self.p1.move("left")
        if keys_pressed[pygame.K_k]:
            self.p1.move("down")
        if keys_pressed[pygame.K_i]:
            self.p1.move("up")
        if keys_pressed[pygame.K_l]:
            self.p1.move("right")
