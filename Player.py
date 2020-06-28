import pygame

default_font = None


class Player:
    def __init__(self, x, y, animation, world, death_anim):
        self.anim = animation
        self.pos = [x, y]
        self.rect = self.anim.current_image.get_rect()
        self.world = world
        self.update_rect_pos()
        self.dead_stage = -1
        self.death_anim = death_anim
        self.death_time = sum(self.death_anim.times)
        global default_font
        default_font = pygame.font.SysFont(pygame.font.get_default_font(), 100)
    
    def move(self, direction):
        if self.dead_stage != -1:
            return
        movements = {"left": lambda x: [self.pos[0] - 1 if self.pos[0] != 0 else self.pos[0], self.pos[1]],
                     "right": lambda x: [self.pos[0] + 1 if self.pos[0] != self.world.world_width-1 else self.pos[0], self.pos[1]],
                     "up": lambda x: [self.pos[0], self.pos[1] - 1 if self.pos[1] != 0 else self.pos[1]],
                     "down": lambda x: [self.pos[0], self.pos[1] + 1 if self.pos[1] != self.world.world_height-1 else self.pos[1]]}
        if direction not in movements:
            print("Given direction to dict 'movements' is not valid, key does not exist.")
            return
        if self.query_board(self.pos[0], self.pos[1]).tile_type.accessible_to.__contains__(direction) and \
                self.query_board(movements[direction](self.pos)[0], movements[direction](self.pos)[1]).tile_type.accessible_from.__contains__(
                    {"left": "right", "right": "left", "up": "down", "down": "up"}[direction]):
            self.pos = movements[direction](self.pos)
            self.update_rect_pos()
    
    def update_rect_pos(self):
        [self.rect.x, self.rect.y] = [self.pos[0] * 50 - 6, self.pos[1] * 50 - 4]
    
    def query_board(self, x, y):
        return self.world.tiles[x][y]
    
    def draw(self, surf, uisurf):
        if self.dead_stage > self.death_time:
            pygame.draw.rect(uisurf, (255, 0, 0), (200, 200, 400, 200))
            global default_font
            
            text_surf: pygame.Surface = default_font.render("You died!", True, (255, 255, 255))
            uisurf.blit(text_surf, (400 - text_surf.get_width() / 2, 300 - text_surf.get_height() / 2))
            return
        if self.dead_stage != -1:
            self.dead_stage += 1
            self.death_anim.update_anim()
            surf.blit(self.death_anim.current_image, self.rect)
        else:
            self.anim.update_anim()
            surf.blit(self.anim.current_image, self.rect)
    
    def die(self):
        if self.dead_stage != -1:
            return
        self.dead_stage = 0
        # print("yeet")
