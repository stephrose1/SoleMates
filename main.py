import sys
import pygame
from socky import Socky
from spritesheet import SpriteSheet
from game import Game, MENU_STATE

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = Socky(SpriteSheet('assets/socky.png'))
game = Game(screen)
game.set_state(MENU_STATE)

game_font = pygame.font.Font("helsinki.ttf", 60)
system_font = pygame.font.SysFont("monospace", 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            game.handle_event(event)

    game.tick()

    # limit the game to 30 fps
    clock.tick(30)
