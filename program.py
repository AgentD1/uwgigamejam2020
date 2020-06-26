import random

import pygame
from World import World
from Player import Player

from camera import Camera
from Tile import Tile
from tiletype import TileType

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

sprite_sheet = pygame.image.load("tiles.png")  # image width / tile width * desired tile width
sprite_sheet = pygame.transform.scale(sprite_sheet, (int(384 / 32 * 50), int(96 / 32 * 50)))


def get_sprite_at_spritesheet_location(x, y):
    return sprite_sheet.subsurface((x * 50, y * 50, 50, 50))


tile_type_test = TileType(get_sprite_at_spritesheet_location(0, 0))

tiles = []
tile_types = []
for x in range(12):
    for y in range(2):
        tile_types.append(TileType(get_sprite_at_spritesheet_location(x, y)))

for x in range(50):
    for y in range(25):
        tiles.append(Tile(x * 50, y * 50, random.choice(tile_types), world_surface))

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
    
    keys_pressed = pygame.key.get_pressed()
    cx = camera.x
    cy = camera.y
    if keys_pressed[pygame.K_w]:
        cy -= 1
    if keys_pressed[pygame.K_s]:
        cy += 1
    if keys_pressed[pygame.K_a]:
        cx -= 1
    if keys_pressed[pygame.K_d]:
        cx += 1
    
    camera.move_bounded(cx, cy, 0, 0, -background_width + display_width, -background_height + display_height)
    # Make sure the camera isn't out of bound
    
    display.fill((0, 0, 0))
    
    camera.start_drawing()
    
    pygame.draw.circle(world_surface, (255, 0, 0), (400, 400), 50)
    
    for tile in tiles:
        tile.draw()
    
    camera.stop_drawing()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
