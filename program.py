import pygame
from World import World
from Player import Player
from controller import Controller
from camera import Camera

pygame.init()

SOMECOLOR = (200, 100, 0)

movingsprites = pygame.sprite.Group()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("UWGI Game Jam 2020: Jacob Parker, James Wigg")

clock = pygame.time.Clock()

world_presets = [["world1"], ["world2"]]  # tile presets for different levels, perhaps make a tile_presets file

background_width = 1600
background_height = 1200
world = World(background_width, background_height, 20, 20, [])

p1 = Player(50, 50, SOMECOLOR)
movingsprites.add(p1)

quitRequested = False

camera = Camera(world.background, display)

controller = Controller(p1,camera)

while not quitRequested:
    controller.check_keys()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitRequested = True
    display.fill((0, 0, 0))
    camera.start_drawing()

    pygame.draw.circle(world.background, (255, 0, 0), (400, 400), 50)
    
    camera.stop_drawing()

    movingsprites.draw(display)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
