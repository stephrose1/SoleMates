import math
import pygame


class Player:
    def __init__(self, clock):
        self.pos = (50, 50)
        self.vel = (0, 0)
        self.dir = math.pi / 4
        self.clock = clock
        self.sprite = Player.create_sprite()
        self.turning = 0
        self.moving = 0

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
        return pygame.transform.rotate(self.sprite, math.degrees(self.dir))

    def __repr__(self):
        (x_pos, y_pos) = self.pos
        (x_vel, y_vel) = self.vel
        turning_dir = 'not turning'
        movement_dir = 'not moving'
        bearing = math.degrees(self.dir)

        if self.turning < 0:
            turning_dir = 'left'
        elif self.turning > 0:
            turning_dir = 'right'

        if self.moving < 0:
            movement_dir = 'backward'
        if self.moving > 0:
            movement_dir = 'forward'

        return (
            "position: ({x_pos:.2f}, {y_pos:.2f}), "
            "velocity: ({x_vel:.2f}, {y_vel:.2f}), "
            "bearing: {bearing:.2f}, "
            "turning: {turning_dir}, "
            "moving: {movement_dir}"
        ).format(
            x_pos=x_pos, y_pos=y_pos, x_vel=x_vel, y_vel=y_vel,
            bearing=bearing, turning_dir=turning_dir, movement_dir=movement_dir
        )

    @classmethod
    def create_sprite(cls):
        sprite = pygame.Surface((100, 100))
        points = ((0, 0), (50, 100), (100, 0))
        pygame.draw.polygon(sprite, (255, 0, 0), points)

        return sprite
