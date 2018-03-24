import sys
import pygame
from player import Player

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = Player(clock)

game_font = pygame.font.Font("helsinki.ttf", 60)
system_font = pygame.font.SysFont("monospace", 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.handle_keydown(event)
        if event.type == pygame.KEYUP:
            player.handle_keyup(event)

    fps_label = system_font.render('%.2f' % clock.get_fps(), True, (255, 0, 0))
    player_debug_label = system_font.render(str(player), True, (255, 0, 0))

    player.update()
    player_sprite = player.render()

    screen.fill(black)
    screen.blit(fps_label, (0, 0))
    screen.blit(player_debug_label, (0, 10))
    screen.blit(player_sprite, player.pos)

    pygame.display.flip()

    # 30 FPS
    clock.tick(30)
