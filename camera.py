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
