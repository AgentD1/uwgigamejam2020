import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        
        self.pos = [x, y]
        
        self.rect = self.image.get_rect()
        self.rect.y = self.pos[0] * 50 - 35
        self.rect.x = self.pos[1] * 50 - 35
    
    def move(self, direction):
        movements = {"left": lambda x: [self.pos[0] - 1, self.pos[1]],
                     "right": lambda x: [self.pos[0] + 1, self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1] - 1],
                     "down": lambda x: [self.pos[0], self.pos[1] + 1]}
        try:
            self.pos = movements[direction](self.pos)
            [self.rect.x, self.rect.y] = [self.pos[0] * 50 - 35, self.pos[1] * 50 - 35]
        except BaseException:
            print("error accessing movements in Player.py")
    
    def query_board(self, x, y, board):
        return type(board[x][y])
