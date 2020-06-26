import pygame
from World import World
from Player import Player

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("UWGI Game Jam 2020: Jacob Parker, James Wigg")

clock = pygame.time.Clock()

background_width = 1600
background_height = 1200

worldSurf = pygame.Surface((background_width, background_height))

quitRequested = False

while not quitRequested:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitRequested = True
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
        #print(event)

    display.fill((255, 0, 0) if pygame.key.get_pressed()[pygame.K_SPACE] else (0, 255, 255))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
