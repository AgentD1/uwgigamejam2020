import pygame
from Player import Player


class Controller:
    def __init__(self, p1, camera, bgw, bgh, dw, dh):
        self.p1 = p1
        self.camera = camera
        self.background_width = bgw
        self.background_height = bgh
        self.display_width = dw
        self.display_height = dh
    
    def check_keys(self):
        
        keys_pressed = pygame.key.get_pressed()
        cx = self.camera.x
        cy = self.camera.y
        if keys_pressed[pygame.K_w]:
            cy -= 1
        if keys_pressed[pygame.K_s]:
            cy += 1
        if keys_pressed[pygame.K_a]:
            cx -= 1
        if keys_pressed[pygame.K_d]:
            cx += 1
        self.camera.move_bounded(cx, cy, 0, 0, -self.background_width + self.display_width,
                                 -self.background_height + self.display_height)
        # Make sure the camera isn't out of bound
        if keys_pressed[pygame.K_j]:
            self.p1.move("left")
        if keys_pressed[pygame.K_k]:
            self.p1.move("down")
        if keys_pressed[pygame.K_i]:
            self.p1.move("up")
        if keys_pressed[pygame.K_l]:
            self.p1.move("right")
