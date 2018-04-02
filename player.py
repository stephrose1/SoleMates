import math
import pygame
import numpy.matlib
from point import rotate, translate, bbox, shear_x

LEFT_KEY = 97
RIGHT_KEY = 100
FORWARD_KEY = 119
BACK_KEY = 115


class Player:
    # coordinates of points of player polygon
    MODEL = [(10, math.sqrt(7500)), (-10, math.sqrt(7500)), (-50, 0), (50, 0)]

    # center of rotation
    MODEL_CENTER = (0, math.sqrt(7500) / 2)

    # how much the player turns per tick
    TURN_SPEED = math.pi / 25

    # how much the player moves per tick
    MOVE_SPEED = 6

    # color of the player
    COLOUR = (255, 0, 0)

    def __init__(self):
        """Set up initial state of the player"""
        # current position of the player
        self.pos = (50, 50)

        # current velocity of the player, as a vector
        self.vel = (0, 0)

        # bearing of the player
        self.dir = math.pi

        # which direction the player is turning
        # -1 : left
        #  1 : right
        #  0 : not turning
        self.turning = 0

        # which direction the player is moving
        # -1 : backward
        #  1 : forward
        #  0 : not moving
        self.moving = 0

    def update_dir(self):
        """update the players bearing"""
        self.dir += self.turning * Player.TURN_SPEED
        self.dir = math.fmod(self.dir, 2 * math.pi)

    def update_vel(self):
        """update the players velocity using the movement direction and bearing"""
        speed = self.moving * Player.MOVE_SPEED
        x_vel = -math.sin(self.dir) * speed
        y_vel = math.cos(self.dir) * speed
        self.vel = (x_vel, y_vel)

    def update_pos(self):
        """update the players position"""
        if self.moving != 0:
            (x_pos, y_pos) = self.pos
            (x_vel, y_vel) = self.vel
            x_pos += x_vel
            y_pos += y_vel

            self.pos = (x_pos, y_pos)

    def update(self):
        """update the player bearing, velocity and position"""
        self.update_dir()
        self.update_vel()
        self.update_pos()

    def render(self):
        """render the player model and return the surface and position on screen where it should be rendered"""
        # this code is yucky, there must be a better way
        model = [rotate(p, self.dir) for p in Player.MODEL]
        center = rotate(Player.MODEL_CENTER, self.dir)

        # model = [shear_x(p, -1) for p in model]
        # center = shear_x(center, -1)

        (min_x, min_y, _, _) = bbox(model)

        model = [translate(p, -min_x, -min_y) for p in model]
        center = translate(center, -min_x, -min_y)

        (_, _, max_x, max_y) = bbox(model)

        sprite = pygame.Surface((math.ceil(max_x), math.ceil(max_y)))
        pygame.draw.polygon(sprite, Player.COLOUR, model)

        (center_x, center_y) = center
        (pos_x, pos_y) = self.pos
        # render_pos = shear_x((pos_x - center_x, pos_y - center_y), -1)
        render_pos = (pos_x - center_x, pos_y - center_y)

        return sprite, render_pos

    def __repr__(self):
        """string representation of the player for debugging"""
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

    def handle_keydown(self, event):
        """handle when player presses a key"""
        if event.key == LEFT_KEY:
            self.turning = - 1
        elif event.key == RIGHT_KEY:
            self.turning = 1
        elif event.key == FORWARD_KEY:
            self.moving = 1
        elif event.key == BACK_KEY:
            self.moving = -1

    def handle_keyup(self, event):
        """handle when player releases a key"""
        if event.key == LEFT_KEY or event.key == RIGHT_KEY:
            self.turning = 0
        if event.key == FORWARD_KEY or event.key == BACK_KEY:
            self.moving = 0
