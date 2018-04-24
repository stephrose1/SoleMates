import sys
import pygame



def healthIndicator(health):
    healthbar = (20, 20, health, 30)
    return healthbar

def livesIndicator(numLives):
    if numLives == 0:
        return pygame.image.load('assets/zerolives.png')
    if numLives == 1:
        return pygame.image.load('assets/onelives.png')
    if numLives == 2:
        return pygame.image.load('assets/twolives.png')
    if numLives == 3:
        return pygame.image.load('assets/threelives.png')
    if numLives == 4:
        return pygame.image.load('assets/fourlives.png')


# For testing:

pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

red = 255, 0, 0
healthBorder = pygame.image.load('assets/healthbar.png')
inventory = pygame.image.load('assets/inventory.png')

# Values from Socky sprite
health = 50
numLives = 3

healthIndicator(health)
livesIndicator(numLives)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # send key events to the player
        if event.type == pygame.KEYDOWN:
            player.handle_keydown(event)
        if event.type == pygame.KEYUP:
            player.handle_keyup(event)


        screen.fill(red, healthIndicator(health))
        screen.blit(livesIndicator(numLives), (150, 15))
        screen.blit(healthBorder, (10, 10))
        screen.blit(inventory, (785, 10))

        pygame.display.flip()

        clock.tick(30)



