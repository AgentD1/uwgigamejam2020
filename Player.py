import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        
        self.pos = [x, y]
        
        self.rect = self.image.get_rect()
        self.rect.y = self.pos[0] * 50 - 34
        self.rect.x = self.pos[1] * 50 - 34
    
    def move(self, direction):
        movements = {"left": lambda x: [self.pos[0] - 1, self.pos[1]],
                     "right": lambda x: [self.pos[0] + 1, self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1] - 1],
                     "down": lambda x: [self.pos[0], self.pos[1] + 1]}
        try:
            self.pos = movements[direction](self.pos)
            [self.rect.x, self.rect.y] = [self.pos[0] * 50 - 34, self.pos[1] * 50 - 34]
        except BaseException:
            print("error accessing movements in Player.py")
    
    def query_board(self, x, y, board):
        return type(board[x][y])
