import sys
import pygame
from socky import Socky
from spritesheet import SpriteSheet

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = Socky(SpriteSheet('assets/socky.png'))

game_font = pygame.font.Font("helsinki.ttf", 60)
system_font = pygame.font.SysFont("monospace", 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # send key events to the player
        if event.type == pygame.KEYDOWN:
            player.handle_keydown(event)
        if event.type == pygame.KEYUP:
            player.handle_keyup(event)

    # render fps label
    fps_label = system_font.render('%.2f' % clock.get_fps(), True, (255, 0, 0))

    # render player debug info (this calls __repr__ on the player)
    player_debug_label = system_font.render(str(player), True, (255, 0, 0))

    # update and render the player
    player.update()
    player_sprite, player_pos = player.render()

    # draw things on the screen
    screen.fill(black)
    screen.blit(fps_label, (0, 0))
    screen.blit(player_debug_label, (0, 10))
    screen.blit(player_sprite, player_pos)

    # flip the buffer
    pygame.display.flip()

    # limit the game to 30 fps
    clock.tick(30)
