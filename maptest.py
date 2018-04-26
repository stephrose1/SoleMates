import sys
import pygame



images = {
    0: pygame.image.load('assets/tiles/0.png'), 6: pygame.image.load('assets/tiles/6.png'),
    7: pygame.image.load('assets/tiles/7.png'), 8: pygame.image.load('assets/tiles/8.png'),
    9: pygame.image.load('assets/tiles/9.png'), 14: pygame.image.load('assets/tiles/14.png'),
    15: pygame.image.load('assets/tiles/15.png'),
    16: pygame.image.load('assets/tiles/16.png'), 17: pygame.image.load('assets/tiles/17.png'),
    18: pygame.image.load('assets/tiles/18.png'), 19: pygame.image.load('assets/tiles/19.png'),
    20: pygame.image.load('assets/tiles/20.png'), 21: pygame.image.load('assets/tiles/21.png'),

    22: pygame.image.load('assets/tiles/22.png'), 23: pygame.image.load('assets/tiles/23.png'),
    24: pygame.image.load('assets/tiles/24.png'), 25: pygame.image.load('assets/tiles/25.png'),
    26: pygame.image.load('assets/tiles/26.png'), 27: pygame.image.load('assets/tiles/27.png'),
    28: pygame.image.load('assets/tiles/28.png'), 29: pygame.image.load('assets/tiles/29.png'),
    30: pygame.image.load('assets/tiles/30.png'), 31: pygame.image.load('assets/tiles/31.png'),
    32: pygame.image.load('assets/tiles/32.png'), 33: pygame.image.load('assets/tiles/33.png'),

    34: pygame.image.load('assets/tiles/34.png'), 35: pygame.image.load('assets/tiles/35.png'),
    36: pygame.image.load('assets/tiles/36.png'), 37: pygame.image.load('assets/tiles/37.png'),
    38: pygame.image.load('assets/tiles/38.png'), 39: pygame.image.load('assets/tiles/39.png'),
    40: pygame.image.load('assets/tiles/40.png'),
    41: pygame.image.load('assets/tiles/41.png'), 42: pygame.image.load('assets/tiles/42.png'),
    45: pygame.image.load('assets/tiles/45.png'), 46: pygame.image.load('assets/tiles/46.png'),

    47: pygame.image.load('assets/tiles/47.png'), 48: pygame.image.load('assets/tiles/48.png'),
    49: pygame.image.load('assets/tiles/49.png'), 50: pygame.image.load('assets/tiles/50.png'),
    52: pygame.image.load('assets/tiles/52.png'), 53: pygame.image.load('assets/tiles/53.png'),
    54: pygame.image.load('assets/tiles/54.png'), 55: pygame.image.load('assets/tiles/55.png'),
    56: pygame.image.load('assets/tiles/56.png'), 57: pygame.image.load('assets/tiles/57.png'),
    58: pygame.image.load('assets/tiles/58.png'), 60: pygame.image.load('assets/tiles/60.png'),

    61: pygame.image.load('assets/tiles/61.png'), 63: pygame.image.load('assets/tiles/63.png'),
    64: pygame.image.load('assets/tiles/64.png'),
    65: pygame.image.load('assets/tiles/65.png'), 66: pygame.image.load('assets/tiles/66.png'),
    68: pygame.image.load('assets/tiles/68.png'), 69: pygame.image.load('assets/tiles/69.png'),
    70: pygame.image.load('assets/tiles/70.png'), 71: pygame.image.load('assets/tiles/71.png'),
    78: pygame.image.load('assets/tiles/78.png'), 79: pygame.image.load('assets/tiles/79.png')

}

#tilemap
tilemap = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [16, 17, 18, 19, 20, 21, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [24, 25, 26, 27, 28, 29, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [32, 33, 34, 35, 36, 37, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7],
    [40, 41, 42, 42, 42, 45, 0, 0, 0, 0, 0, 0, 0, 0, 14, 15],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23],
    [30, 31, 0, 0, 0, 0, 48, 49, 50, 50, 50, 52, 53, 0, 0, 0],
    [38, 39, 0, 63, 0, 0, 56, 57, 58, 58, 58, 60, 61, 0, 0, 0],
    [46, 47, 70, 71, 0, 0, 56, 57, 58, 58, 58, 60, 61, 0, 0, 0],
    [54, 55, 78, 79, 0, 0, 64, 65, 66, 66, 66, 68, 69, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#gamedimensions
TILESIZE = 64
MAPWIDTH = 16
MAPHEIGHT = 12


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(images[tilemap[row][column]],(column*TILESIZE, row*TILESIZE))


    pygame.display.flip()

    clock.tick(30)