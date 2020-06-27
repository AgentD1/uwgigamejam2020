import pygame


class Player:
    def __init__(self, x, y, image, world):
        super().__init__()
        
        self.image = image
        
        self.pos = [x, y]
        
        self.rect = self.image.get_rect()
        
        self.world = world
        
        self.update_rect_pos()
    
    def move(self, direction):
        movements = {"left": lambda x: [self.pos[0] - 1, self.pos[1]],
                     "right": lambda x: [self.pos[0] + 1, self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1] - 1],
                     "down": lambda x: [self.pos[0], self.pos[1] + 1]}
        try:
            
            self.pos = movements[direction](self.pos)
            self.update_rect_pos()
        except BaseException:
            print("error accessing movements in Player.py")
    
    def update_rect_pos(self):
        [self.rect.x, self.rect.y] = [self.pos[0] * 50 - 6, self.pos[1] * 50 - 4]
    
    def query_board(self, x, y, board):
        return type(board[x][y])
    
    def draw(self, surf):
        surf.blit(self.image, self.rect)
