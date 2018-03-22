import sys
import pygame

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    myfont = pygame.font.Font("helsinki.ttf", 60)

    label = myfont.render("Welcome to SoleMates!", 1, (255, 255, 0))
    screen.fill(black)
    screen.blit(label, (100, 100))
    pygame.display.flip()

