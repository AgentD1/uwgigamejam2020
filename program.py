import pygame
from World import World
from Player import Player

from camera import Camera

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("UWGI Game Jam 2020: Jacob Parker, James Wigg")

clock = pygame.time.Clock()

background_width = 1600
background_height = 1200

world_surface = pygame.Surface((background_width, background_height))
camera = Camera(world_surface, display)


quitRequested = False

while not quitRequested:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitRequested = True
        elif event.type == pygame.KEYDOWN:
            """if event.key == pygame.K_w:
                camera.y += 1
            elif event.key == pygame.K_s:
                camera.y -= 1
            elif event.key == pygame.K_a:
                camera.x += 1
            elif event.key == pygame.K_d:
                camera.x -= 1"""
        elif event.type == pygame.KEYUP:
            pass

        print(event)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        camera.y += 1
    if keys_pressed[pygame.K_s]:
        camera.y -= 1
    if keys_pressed[pygame.K_a]:
        camera.x += 1
    if keys_pressed[pygame.K_d]:
        camera.x -= 1
    
    display.fill((0, 0, 0))
    
    camera.start_drawing()
    
    pygame.draw.circle(world_surface, (255, 0, 0), (400, 400), 50)
    
    camera.stop_drawing()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
