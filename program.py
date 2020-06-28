import random

import pygame

from Battery import Battery
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
tile_sprite_sheet = pygame.transform.scale(tile_sprite_sheet, (int(tile_sprite_sheet.get_width() / 32 * 50), int(tile_sprite_sheet.get_height() / 32 * 50)))

player_sprite_sheet = pygame.image.load("player.png")
player_sprite_sheet = pygame.transform.scale(player_sprite_sheet, (int(player_sprite_sheet.get_width() / 32 * 64), int(player_sprite_sheet.get_height() / 32 * 64)))


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

tile_types = {}

world = World(background_width, background_height, 20, 20, [], tile_types)

p1anim = Animation([get_sprite_at_player_spritesheet_location(0, 0),
                    get_sprite_at_player_spritesheet_location(1, 0),
                    get_sprite_at_player_spritesheet_location(2, 0),
                    get_sprite_at_player_spritesheet_location(3, 0),
                    get_sprite_at_player_spritesheet_location(4, 0),
                    get_sprite_at_player_spritesheet_location(5, 0),
                    get_sprite_at_player_spritesheet_location(6, 0),
                    get_sprite_at_player_spritesheet_location(7, 0)], [20, 20, 20, 20, 20, 20, 20, 20])

p1deathAnim = Animation([get_sprite_at_player_spritesheet_location(0, 1),
                         get_sprite_at_player_spritesheet_location(1, 1),
                         get_sprite_at_player_spritesheet_location(2, 1),
                         get_sprite_at_player_spritesheet_location(3, 1),
                         get_sprite_at_player_spritesheet_location(4, 1),
                         get_sprite_at_player_spritesheet_location(5, 1),
                         get_sprite_at_player_spritesheet_location(6, 1),
                         get_sprite_at_player_spritesheet_location(7, 1)], [10, 10, 10, 10, 10, 10, 10, 10])

batteryNotMainAnim = Animation([get_sprite_at_tiles_spritesheet_location(0, 3),
                             get_sprite_at_tiles_spritesheet_location(1, 3),
                             get_sprite_at_tiles_spritesheet_location(2, 3)], [4, 4, 3])

batteryMainAnim = Animation([get_sprite_at_tiles_spritesheet_location(4, 3),
                                get_sprite_at_tiles_spritesheet_location(5, 3),
                                get_sprite_at_tiles_spritesheet_location(6, 3)], [4, 4, 3])

p1 = Player(1, 1, p1anim, world, p1deathAnim)

quitRequested = False

tile_type_test = TileType(get_sprite_at_tiles_spritesheet_location(0, 0), None, None)

animations_to_update = [batteryMainAnim, batteryNotMainAnim]


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
    tile_types["batteryMain"] = TileType(batteryMainAnim, ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    tile_types["batteryNotMain"] = TileType(batteryNotMainAnim, ["down", "up", "left", "right"], ["down", "up", "left", "right"])
    tile_types["batteryOff"] = TileType(get_sprite_at_tiles_spritesheet_location(3, 3), ["down", "up", "left", "right"], ["down", "up", "left", "right"])


define_tiles()

for (key, value) in tile_types.items():
    value.name = key

tile_types_generatable = []

for (key, value) in tile_types.items():
    if 'p' not in key:
        tile_types_generatable.append(value)

tiles = []

world.tiles = tiles

camera = Camera(world.background, display)

controller = Controller(p1, camera, background_width, background_height, display_width, display_height)

for x in range(32):
    tiles.append([])
    for y in range(24):
        tiles[x].append(Tile(x * 50, y * 50, random.choice(list(tile_types_generatable)), camera.world_surface))

batteries = []


# pycharm being stupid again
# noinspection PyUnresolvedReferences
def create_battery(x, y, reach):
    if x + reach > len(tiles) - 1 or x - reach < 0 or y + reach > len(tiles[0]) - 1 or y - reach < 0:
        return
    my_tile = tiles[x][y]
    main_battery = my_tile.tile_type == tile_types["batteryMain"]
    battery_on = not (my_tile.tile_type == tile_types["batteryOff"])
    surrounding_tiles = []
    for offset in range(1, reach + 1):
        surrounding_tiles.append(tiles[x + offset][y])
        surrounding_tiles.append(tiles[x - offset][y])
        surrounding_tiles.append(tiles[x][y + offset])
        surrounding_tiles.append(tiles[x][y - offset])
    batteries.append(Battery(x, y, world, main_battery, battery_on, surrounding_tiles, "", ""))


for i in tiles:
    for tile in i:
        if tile.tile_type == tile_types["batteryMain"] or tile.tile_type == tile_types["batteryOff"] or tile.tile_type == tile_types["batteryNotMain"]:
            create_battery(int(tile.x / 50), int(tile.y / 50), 2)
            # batteries.append(Battery(tile.x / 50, tile.y / 50, tile.tile_type == tile_types["batteryMain"], tile.tile_type != tile_types["batteryOff"], [tiles[int(tile.x / 50 + 1)][int(tile.y / 50)]], "up", "up"))


def battery_at_location(x, y):
    for b in batteries:
        if b.x == x and b.y == y:
            return b
    return None


uisurf = pygame.Surface((display_width, display_height), pygame.SRCALPHA)

while not quitRequested:
    controller.check_keys()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitRequested = True
        elif event.type == pygame.KEYDOWN:
            battery_here = battery_at_location(p1.pos[0], p1.pos[1])
            if battery_here is not None:
                if event.key == pygame.K_o:
                    battery_here.rotate(-1)
                elif event.key == pygame.K_p:
                    battery_here.rotate(1)
            if event.key == pygame.K_g:
                p1.die()
            elif event.key == pygame.K_t:
                print(world.find_connected_battery_locations(p1.pos[0], p1.pos[1]))
            """if event.key == pygame.K_o:
                # pycharm has big-brain't
                # noinspection PyTypeChecker,PyUnresolvedReferences
                world.tiles[p1.pos[0]][p1.pos[1]] = Tile(p1.pos[0] * 50, p1.pos[1] * 50, tile_types[world.tile_rotated_relative(world.tiles[p1.pos[0]][p1.pos[1]].tile_type.name, True)], camera.world_surface)
            if event.key == pygame.K_p:
                # noinspection PyTypeChecker,PyUnresolvedReferences
                world.tiles[p1.pos[0]][p1.pos[1]] = Tile(p1.pos[0] * 50, p1.pos[1] * 50, tile_types[world.tile_rotated_relative(world.tiles[p1.pos[0]][p1.pos[1]].tile_type.name, False)], camera.world_surface)
            """
            """elif event.key == pygame.K_s:
                camera.y -= 1
            elif event.key == pygame.K_a:
                camera.x += 1
            elif event.key == pygame.K_d:
                camera.x -= 1"""
        elif event.type == pygame.KEYUP:
            pass
    
    keys_pressed = pygame.key.get_pressed()
    
    camera.move_bounded(p1.rect.x - display_width / 2 + p1.rect.width / 2,
                        p1.rect.y - display_height / 2 + p1.rect.height / 2, 0, 0,
                        -background_width + display_width,
                        -background_height + display_height)
    # Make sure the camera isn't out of bound
    
    uisurf.fill((0, 0, 0, 0))
    display.fill((0, 0, 0))
    camera.start_drawing()
    
    # pygame.draw.circle(world.background, (255, 0, 0), (400, 400), 50)
    
    for anim in animations_to_update:
        anim.update_anim()
    
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y].draw()
    
    p1.draw(world.background, uisurf)
    
    camera.stop_drawing()
    pygame.display.get_surface().blit(uisurf, (0, 0))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit(0)
