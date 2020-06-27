import pygame


class Player:
    def __init__(self, x, y, animation, world):
        super().__init__()
        
        self.anim = animation
        
        self.pos = [x, y]
        
        self.rect = self.anim.current_image.get_rect()
        
        self.world = world
        
        self.update_rect_pos()
    
    def move(self, direction):
        movements = {"left": lambda x: [self.pos[0] - 1 if self.pos[0] != 0 else self.pos[0], self.pos[1]],
                     "right": lambda x: [self.pos[0] + 1 if self.pos[0] != 31 else self.pos[0], self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1] - 1 if self.pos[1] != 0 else self.pos[1]],
                     "down": lambda x: [self.pos[0], self.pos[1] + 1 if self.pos[1] != 23 else self.pos[1]]}
        try:  # why is this here lol
            if self.query_board(self.pos[0], self.pos[1]).tile_type.accessible_to.__contains__(direction) and \
                    self.query_board(movements[direction](self.pos)[0], movements[direction](self.pos)[1]).tile_type.accessible_from.__contains__(
                        {"left": "right", "right": "left", "up": "down", "down": "up"}[direction]):
                self.pos = movements[direction](self.pos)
                self.update_rect_pos()
        finally:
            pass
    
    def update_rect_pos(self):
        [self.rect.x, self.rect.y] = [self.pos[0] * 50 - 6, self.pos[1] * 50 - 4]
    
    def query_board(self, x, y):
        return self.world.tiles[x][y]
    
    def draw(self, surf):
        self.anim.update_anim()
        surf.blit(self.anim.current_image, self.rect)
