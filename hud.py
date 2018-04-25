import sys
import pygame


class HUD(pygame.sprite.Sprite):

    def __init__(self, health, numlives):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.numlives = numlives


    def health_indicator(self, health):
        healthbar = (20, 20, health, 30)
        healthborder = pygame.image.load('assets/healthbar.png')
        red = 255, 0, 0

        pygame.draw.rect(screen, red, healthbar)
        screen.blit(healthborder, (10, 10))

    def lives_indicator(self, numlives):
        if numlives == 0:
            livesGraphic = pygame.image.load('assets/zerolives.png')
        if numlives == 1:
            livesGraphic = pygame.image.load('assets/onelives.png')
        if numlives == 2:
            livesGraphic = pygame.image.load('assets/twolives.png')
        if numlives == 3:
            livesGraphic = pygame.image.load('assets/threelives.png')
        if numlives == 4:
            livesGraphic = pygame.image.load('assets/fourlives.png')

        screen.blit(livesGraphic, (150, 15))

    def inventory_display(self):
        inventory = pygame.image.load('assets/inventory.png')
        screen.blit(inventory, (785, 10))

    def refresh_hud(self) :
        self.health_indicator(self.health)
        self.lives_indicator(self.numlives)
        self.inventory_display()


# For testing:

pygame.init()

size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        hudisplay = HUD(50, 1)
        hudisplay.refresh_hud()

        pygame.display.flip()

        clock.tick(30)



