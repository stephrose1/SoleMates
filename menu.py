#Reference tutorial: https://nebelprog.wordpress.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/

import pygame

pygame.init()

class MenuItem(pygame.font.Font):
    def __init__(self, text, font= 'helsinki.ttf', font_size= 45,
                 font_color = (0, 0, 0), xy= (0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x, self.pos_y = xy
        self.position = xy

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def is_mouse_over(self, xy):
        posx, posy = xy
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and (posy >= self.pos_y and posy <= self.pos_y + self.height):
            return True
        return False

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
class Menu():
    def __init__(self, screen, items, bg_color =(252, 179, 53), font=None):

        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self. screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item)

            total_height = len(items) * menu_item.height
            pos_x = (self.screen_width / 2) - (menu_item.width / 2)
            pos_y = (self.screen_height / 2) - (total_height / 2) + ((index * 2) +
                                                                     index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def run(self):
        mainloop = True
        while mainloop:

            #Frame speed 30fps
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            self.screen.fill(self.bg_color)

            for item in self.items:
                if item.is_mouse_over(pygame.mouse.get_pos()):
                    item.set_font_color((255, 255, 255))
                else:
                    item.set_font_color((0, 0, 0))
                self.screen.blit(item.label, item.position)
            mouse_test = pygame.mouse.get_pos()
            print(mouse_test)

            pygame.display.flip()

if __name__ == "__main__":
    size = width, height = 1024, 768
    menu_items = ('Level One', 'Level Two', 'Level Three', 'Level Four', 'Bonus')

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Sole Mates Menu')
    menu = Menu(screen, menu_items)
    menu.run()




