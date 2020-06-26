import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        #self.image.fill(200, 200, 0)

        self.pos = [x, y]

    def move(self, direction):
        movements = {"left": lambda x: [self.pos[0]-1, self.pos[1]],
                     "right": lambda x: [self.pos[0]+1, self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1]-1],
                     "down": lambda x: [self.pos[0], self.pos[1]+1]}
        try:
            self.pos = movements[direction](self.pos)
        except BaseException:
            print("error")

    def query_board(self, x, y, board):
        return type(board[x][y])
