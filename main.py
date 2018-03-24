import sys
import pygame

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game_font = pygame.font.Font("helsinki.ttf", 60)
system_font = pygame.font.SysFont("monospace", 20)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    fps_label = system_font.render('%.2f' % clock.get_fps(), True, (255, 0, 0))
    screen.fill(black)
    screen.blit(fps_label, (0, 0))
    pygame.display.flip()

    # 30 FPS
    clock.tick(30)
