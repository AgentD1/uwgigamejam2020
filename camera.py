import pygame


class Camera:
    def __init__(self, the_world_surface, the_display):
        self.x = 0
        self.y = 0
        self.world_surface = the_world_surface
        self.display = the_display
    
    def start_drawing(self):
        self.world_surface.fill((255, 255, 255))
    
    
    def stop_drawing(self):
        self.display.blit(self.world_surface, (-self.x, -self.y))
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def move_bounded(self, x, y, bx, by, bw, bh):
        if x < bx:
            x = bx
        elif x > bx - bw:
            x = bx - bw
        if y < by:
            y = by
        elif y > by - bh:
            y = by - bh
        
        self.x = x
        self.y = y
