#Reference tutorial: https://nebelprog.wordpress.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/

import pygame

pygame.init()

class Menu():
    def __init__(self, screen, items, bg_color =(252, 179, 53), font= 'helsinki.ttf', font_size= 60,
                 font_color = (0, 0, 0)):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self. screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.screen_width / 2) - (width / 2)

            #menu height
            total_height = len(items) * height
            posy = (self.screen_height / 2) - (total_height / 2) + (index * height)
            self.items.append([item, label, (width, height), (posx, posy)])

    def run(self):
        mainloop = True
        while mainloop:

            #Frame speed 30fps
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            self.screen.fill(self.bg_color)
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()

if __name__ == "__main__":
    size = width, height = 1024, 768
    menu_items = ('Level One', 'Level Two', 'Level Three', 'Level Four', 'Bonus')

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Sole Mates Menu')
    menu = Menu(screen, menu_items)
    menu.run()




