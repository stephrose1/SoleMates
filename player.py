import math
import pygame
import numpy.matlib

LEFT_KEY = 100
RIGHT_KEY = 97
FORWARD_KEY = 119
BACK_KEY = 115


class Player:
    MODEL = [(0, math.sqrt(7500)), (-50, 0), (50, 0)]
    MODEL_CENTER = (0, math.sqrt(7500) / 2)  # center of rotation
    TURN_SPEED = math.pi / 25
    MOVE_SPEED = 6
    COLOUR = (255, 0, 0)

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

    def compute_vel(self):
        speed = self.moving * Player.MOVE_SPEED
        x_vel = math.sin(self.dir) * speed
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

    # !!! TODO: Refactor this into a library
    def render(self):
        # create rotation matrix
        rot = numpy.matlib.matrix(
            ([math.cos(self.dir), -math.sin(self.dir)],
             [math.sin(self.dir), math.cos(self.dir)])
        )

        points = list()
        # rotate model
        for point in Player.MODEL:
            points.append(numpy.matrix(point) * rot)

        # rotate center
        center_vec = numpy.matrix(Player.MODEL_CENTER) * rot

        # find bottom left corner
        origin_y = 0
        origin_x = 0
        for point in points:
            [[x, y]] = point.tolist()

            if x < origin_x:
                origin_x = x

            if y < origin_y:
                origin_y = y

        # translate points to origin
        polygon_points = list()
        for point in points:
            [[x, y]] = point.tolist()
            polygon_points.append((x - origin_x, y - origin_y))

        # translate center
        [[center_x, center_y]] = center_vec.tolist()
        center_x -= origin_x
        center_y -= origin_y

        # get size of bounding box
        max_x = 0
        max_y = 0
        for point in polygon_points:
            (x, y) = point
            if x > max_x:
                max_x = x

            if y > max_y:
                max_y = y

        # now ready to render
        sprite = pygame.Surface((math.ceil(max_x), math.ceil(max_y)))
        pygame.draw.polygon(sprite, Player.COLOUR, polygon_points)

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
            self.turning = -1
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
