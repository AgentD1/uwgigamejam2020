import random

import pygame
from World import World
from Player import Player
from controller import Controller
from camera import Camera
from Tile import Tile
from tiletype import TileType

pygame.init()

SOMECOLOR = (200, 100, 0)

movingsprites = pygame.sprite.Group()

tile_sprite_sheet = pygame.image.load("tiles.png")  # image width / tile width * desired tile width
tile_sprite_sheet = pygame.transform.scale(tile_sprite_sheet, (int(384 / 32 * 50), int(96 / 32 * 50)))

player_sprite_sheet = pygame.image.load("player.png")


def get_sprite_at_tiles_spritesheet_location(x, y):
    return tile_sprite_sheet.subsurface((x * 50, y * 50, 50, 50))


def get_sprite_at_player_spritesheet_location(x, y):
    return player_sprite_sheet.subsurface((x * 32, y * 32, 32, 32))


display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("UWGI Game Jam 2020: Jacob Parker, James Wigg")

clock = pygame.time.Clock()

world_presets = [["world1"], ["world2"]]  # tile presets for different levels, perhaps make a tile_presets file

background_width = 1600
background_height = 1200
world = World(background_width, background_height, 20, 20, [])

p1 = Player(50, 50, get_sprite_at_player_spritesheet_location(0, 0))
movingsprites.add(p1)

quitRequested = False

tile_type_test = TileType(get_sprite_at_tiles_spritesheet_location(0, 0), None, None)

tiles = []
tile_types = []
for x in range(12):
    for y in range(2):
        tile_types.append(TileType(get_sprite_at_tiles_spritesheet_location(x, y), None, None))

world.tiles = tiles

camera = Camera(world.background, display)

controller = Controller(p1, camera, background_width, background_height, display_width, display_height)

for x in range(32):
    for y in range(24):
        tiles.append(Tile(x * 50, y * 50, random.choice(tile_types), camera.world_surface))

while not quitRequested:
    controller.check_keys()
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
    """cx = camera.x
    cy = camera.y
    if keys_pressed[pygame.K_w]:
        cy -= 1
    if keys_pressed[pygame.K_s]:
        cy += 1
    if keys_pressed[pygame.K_a]:
        cx -= 1
    if keys_pressed[pygame.K_d]:
        cx += 1"""
    
    camera.move_bounded(p1.pos[0] - display_width / 2, p1.pos[1] - display_height / 2, 0, 0,
                        -background_width + display_width,
                        -background_height + display_height)
    # Make sure the camera isn't out of bound
    
    display.fill((0, 0, 0))
    camera.start_drawing()
    
    pygame.draw.circle(world.background, (255, 0, 0), (400, 400), 50)
    
    for tile in tiles:
        tile.draw()
    
    movingsprites.draw(world.background)
    
    camera.stop_drawing()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
