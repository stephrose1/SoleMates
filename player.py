import math
import pygame


class Player:
    def __init__(self, clock):
        self.pos = (50, 50)
        self.vel = (0, 0)
        self.clock = clock
        self.sprite = Player.create_sprite()

    def get_speed(self):
        (x, y) = self.vel
        return abs(math.sqrt(math.pow(x, 2) + math.pow(x, 2)))

    def update(self):
        if self.get_speed() > 0:
            (x_pos, y_pos) = self.pos
            (x_vel, y_vel) = self.vel
            x_pos += x_vel
            y_pos += y_vel

            self.pos = (x_pos, y_pos)

    def render(self):
        return self.sprite

    @classmethod
    def create_sprite(cls):
        sprite = pygame.Surface((100, 100))
        points = ((0, 0), (50, 100), (100, 0))
        pygame.draw.polygon(sprite, (255, 0, 0), points)

        return sprite
