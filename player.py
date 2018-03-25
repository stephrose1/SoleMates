import math
import pygame
import numpy.matlib
from point import rotate, translate, bbox

LEFT_KEY = 97
RIGHT_KEY = 100
FORWARD_KEY = 119
BACK_KEY = 115


class Player:
    MODEL = [(10, math.sqrt(7500)), (-10, math.sqrt(7500)), (-50, 0), (50, 0)]
    MODEL_CENTER = (0, math.sqrt(7500) / 2)  # center of rotation
    TURN_SPEED = math.pi / 25
    MOVE_SPEED = 6
    COLOUR = (255, 0, 0)

    def __init__(self, clock):
        self.pos = (50, 50)
        self.vel = (0, 0)
        self.dir = math.pi
        self.clock = clock
        self.sprite = Player.create_sprite()
        self.turning = 0
        self.moving = 0

    def get_speed(self):
        (x, y) = self.vel
        return abs(math.sqrt(math.pow(x, 2) + math.pow(x, 2)))

    def compute_vel(self):
        speed = self.moving * Player.MOVE_SPEED
        x_vel = -math.sin(self.dir) * speed
        y_vel = math.cos(self.dir) * speed
        self.vel = (x_vel, y_vel)

    def update(self):
        self.dir += self.turning * Player.TURN_SPEED
        self.dir = math.fmod(self.dir, 2 * math.pi)
        self.compute_vel()

        if self.get_speed() > 0:
            (x_pos, y_pos) = self.pos
            (x_vel, y_vel) = self.vel
            x_pos += x_vel
            y_pos += y_vel

            self.pos = (x_pos, y_pos)

    def render(self):
        model = [rotate(p, self.dir) for p in Player.MODEL]
        center = rotate(Player.MODEL_CENTER, self.dir)

        (min_x, min_y, _, _) = bbox(model)

        model = [translate(p, -min_x, -min_y) for p in model]
        center = translate(center, -min_x, -min_y)

        (_, _, max_x, max_y) = bbox(model)

        sprite = pygame.Surface((math.ceil(max_x), math.ceil(max_y)))
        pygame.draw.polygon(sprite, Player.COLOUR, model)

        (center_x, center_y) = center
        (pos_x, pos_y) = self.pos
        render_pos = (pos_x - center_x, pos_y - center_y)
        return sprite, render_pos

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

    def handle_keydown(self, event):
        if event.key == LEFT_KEY:
            self.turning = - 1
        elif event.key == RIGHT_KEY:
            self.turning = 1
        elif event.key == FORWARD_KEY:
            self.moving = 1
        elif event.key == BACK_KEY:
            self.moving = -1

    def handle_keyup(self, event):
        if event.key == LEFT_KEY or event.key == RIGHT_KEY:
            self.turning = 0
        if event.key == FORWARD_KEY or event.key == BACK_KEY:
            self.moving = 0
