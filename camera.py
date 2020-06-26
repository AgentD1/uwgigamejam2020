import pygame

world_surface = None
display = None


class Camera:
    def __init__(self, the_world_surface, the_display):
        self.x = 0
        self.y = 0
        global world_surface
        world_surface = the_world_surface
        global display
        display = the_display
    
    def start_drawing(self):
        world_surface.fill((255, 255, 255))
        self.draw_cool_pattern_for_testing_purposes()
    
    def draw_cool_pattern_for_testing_purposes(self):
        inverted = False
        for x in range(0, world_surface.get_width(), 50):
            for y in range(0, world_surface.get_height(), 50):
                if inverted:
                    pygame.draw.rect(world_surface, (255, 0, 0), (x, y, 50, 50))
                else:
                    pygame.draw.rect(world_surface, (0, 255, 0), (x, y, 50, 50))
                inverted = not inverted
            inverted = not inverted
    
    def stop_drawing(self):
        display.blit(world_surface, (-self.x, -self.y))
    
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
