import random

import pygame
from World import World
from Player import Player
from controller import Controller
from camera import Camera
from Tile import Tile
from tiletype import TileType
from Animation import Animation

pygame.init()

# SOMECOLOR = (200, 100, 0)

# movingsprites = pygame.sprite.Group()

tile_sprite_sheet = pygame.image.load("tiles.png")  # image width / tile width * desired tile width
tile_sprite_sheet = pygame.transform.scale(tile_sprite_sheet, (int(384 / 32 * 50), int(160 / 32 * 50)))

player_sprite_sheet = pygame.image.load("player.png")
player_sprite_sheet = pygame.transform.scale(player_sprite_sheet, (int(256 / 32 * 64), int(32 / 32 * 64)))


def get_sprite_at_tiles_spritesheet_location(x, y):
    return tile_sprite_sheet.subsurface((x * 50, y * 50, 50, 50))


def get_sprite_at_player_spritesheet_location(x, y):
    return player_sprite_sheet.subsurface((x * 64, y * 64, 64, 64))


display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("UW GI Game Jam 2020: Jacob Parker, James Wigg")

clock = pygame.time.Clock()

world_presets = [["world1"], ["world2"]]  # tile presets for different levels, perhaps make a tile_presets file

background_width = 1600
background_height = 1200
world = World(background_width, background_height, 20, 20, [])

p1anim = Animation([get_sprite_at_player_spritesheet_location(0, 0),
                    get_sprite_at_player_spritesheet_location(1, 0),
                    get_sprite_at_player_spritesheet_location(2, 0),
                    get_sprite_at_player_spritesheet_location(3, 0),
                    get_sprite_at_player_spritesheet_location(4, 0),
                    get_sprite_at_player_spritesheet_location(5, 0),
                    get_sprite_at_player_spritesheet_location(6, 0),
                    get_sprite_at_player_spritesheet_location(7, 0)], [20, 20, 20, 20, 20, 20, 20, 20])

p1 = Player(1, 1, p1anim, world)

quitRequested = False

tile_type_test = TileType(get_sprite_at_tiles_spritesheet_location(0, 0), None, None)

tile_types = {}


# big, collapse it if you want to
def define_tiles():
    # Tile naming scheme: [udlr][pn/] directions powered/notpowered/nothing
    tile_types["ud/"] = TileType(get_sprite_at_tiles_spritesheet_location(0, 0), ["up", "down"], ["up", "down"])
    tile_types["lr/"] = TileType(get_sprite_at_tiles_spritesheet_location(1, 0), ["left", "right"], ["left", "right"])
    tile_types["dr/"] = TileType(get_sprite_at_tiles_spritesheet_location(2, 0), ["down", "right"], ["down", "right"])
    tile_types["dl/"] = TileType(get_sprite_at_tiles_spritesheet_location(3, 0), ["down", "left"], ["down", "left"])
    tile_types["udn"] = TileType(get_sprite_at_tiles_spritesheet_location(4, 0), ["up", "down"], ["up", "down"])
    tile_types["lrn"] = TileType(get_sprite_at_tiles_spritesheet_location(5, 0), ["left", "right"], ["left", "right"])
    tile_types["drn"] = TileType(get_sprite_at_tiles_spritesheet_location(6, 0), ["down", "right"], ["down", "right"])
    tile_types["dln"] = TileType(get_sprite_at_tiles_spritesheet_location(7, 0), ["down", "left"], ["down", "left"])
    tile_types["udp"] = TileType(get_sprite_at_tiles_spritesheet_location(8, 0), ["up", "down"], ["up", "down"])
    tile_types["lrp"] = TileType(get_sprite_at_tiles_spritesheet_location(9, 0), ["left", "right"], ["left", "right"])
    tile_types["drp"] = TileType(get_sprite_at_tiles_spritesheet_location(10, 0), ["down", "right"], ["down", "right"])
    tile_types["dlp"] = TileType(get_sprite_at_tiles_spritesheet_location(11, 0), ["down", "left"], ["down", "left"])
    tile_types["ulr/"] = TileType(get_sprite_at_tiles_spritesheet_location(0, 1), ["up", "left", "right"], ["up", "left", "right"])
    tile_types["udl/"] = TileType(get_sprite_at_tiles_spritesheet_location(1, 1), ["up", "left", "down"], ["up", "left", "down"])
    tile_types["ur/"] = TileType(get_sprite_at_tiles_spritesheet_location(2, 1), ["up", "right"], ["up", "right"])
    tile_types["ul/"] = TileType(get_sprite_at_tiles_spritesheet_location(3, 1), ["up", "left"], ["up", "left"])
    tile_types["ulrn"] = TileType(get_sprite_at_tiles_spritesheet_location(4, 1), ["up", "left", "right"], ["up", "left", "right"])
    tile_types["udln"] = TileType(get_sprite_at_tiles_spritesheet_location(5, 1), ["up", "left", "down"], ["up", "left", "down"])
    tile_types["urn"] = TileType(get_sprite_at_tiles_spritesheet_location(6, 1), ["up", "right"], ["up", "right"])
    tile_types["uln"] = TileType(get_sprite_at_tiles_spritesheet_location(7, 1), ["up", "left"], ["up", "left"])
    tile_types["ulrp"] = TileType(get_sprite_at_tiles_spritesheet_location(8, 1), ["up", "left", "right"], ["up", "left", "right"])
    tile_types["udlp"] = TileType(get_sprite_at_tiles_spritesheet_location(9, 1), ["up", "left", "down"], ["up", "left", "down"])
    tile_types["urp"] = TileType(get_sprite_at_tiles_spritesheet_location(10, 1), ["up", "right"], ["up", "right"])
    tile_types["ulp"] = TileType(get_sprite_at_tiles_spritesheet_location(11, 1), ["up", "left"], ["up", "left"])
    tile_types["dlr/"] = TileType(get_sprite_at_tiles_spritesheet_location(0, 2), ["down", "right", "left"], ["down", "right", "left"])
    tile_types["udr/"] = TileType(get_sprite_at_tiles_spritesheet_location(1, 2), ["down", "up", "right"], ["down", "up", "right"])
    tile_types["udlr/"] = TileType(get_sprite_at_tiles_spritesheet_location(2, 2), ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    tile_types[""] = TileType(get_sprite_at_tiles_spritesheet_location(3, 2), ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    tile_types["dlrn"] = TileType(get_sprite_at_tiles_spritesheet_location(4, 2), ["down", "right", "left"], ["down", "right", "left"])
    tile_types["udrn"] = TileType(get_sprite_at_tiles_spritesheet_location(5, 2), ["down", "up", "right"], ["down", "up", "right"])
    tile_types["udlrn"] = TileType(get_sprite_at_tiles_spritesheet_location(6, 2), ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    tile_types["dlrp"] = TileType(get_sprite_at_tiles_spritesheet_location(8, 2), ["down", "right", "left"], ["down", "right", "left"])
    tile_types["udrp"] = TileType(get_sprite_at_tiles_spritesheet_location(9, 2), ["down", "up", "right"], ["down", "up", "right"])
    tile_types["udlrp"] = TileType(get_sprite_at_tiles_spritesheet_location(10, 2), ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    # Special tiles
    tile_types["battery"] = TileType(get_sprite_at_tiles_spritesheet_location(1, 3), [], [])


define_tiles()

tiles = []

world.tiles = tiles

camera = Camera(world.background, display)

controller = Controller(p1, camera, background_width, background_height, display_width, display_height)

for x in range(32):
    tiles.append([])
    for y in range(24):
        tiles[x].append(Tile(x * 50, y * 50, random.choice(list(tile_types.values())), camera.world_surface))

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
    
    camera.move_bounded(p1.rect.x - display_width / 2 + p1.rect.width / 2,
                        p1.rect.y - display_height / 2 + p1.rect.height / 2, 0, 0,
                        -background_width + display_width,
                        -background_height + display_height)
    # Make sure the camera isn't out of bound
    
    display.fill((0, 0, 0))
    camera.start_drawing()
    
    # pygame.draw.circle(world.background, (255, 0, 0), (400, 400), 50)
    
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y].draw()
    
    p1.draw(world.background)
    
    camera.stop_drawing()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
