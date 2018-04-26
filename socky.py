from animation import Animation

LEFT_KEY = 97
RIGHT_KEY = 100
UP_KEY = 119
DOWN_KEY = 115

FACING_LEFT = 0
FACING_RIGHT = 1


class Socky:
    # how much the player moves per tick
    MOVE_SPEED = 6

    # sprite data
    SPR_H = 32
    SPR_IDLE_L = 32
    SPR_WALK_L = 58



    def __init__(self, spritesheet):
        """Set up initial state of the player"""
        # current position of the player
        self.pos = (50, 50)

        # current velocity of the player, as a vector
        self.vel = (0, 0)

        # which way socky is facing
        self.facing = FACING_RIGHT

        self.idle_right_cycle = spritesheet.load_anim(0, Socky.SPR_IDLE_L, Socky.SPR_H, 2, 500)
        self.idle_left_cycle = spritesheet.load_anim(1, Socky.SPR_IDLE_L, Socky.SPR_H, 2, 500)
        self.walk_right_cycle = spritesheet.load_anim(2, Socky.SPR_WALK_L, Socky.SPR_H, 6, 400)
        self.walk_left_cycle = spritesheet.load_anim(3, Socky.SPR_WALK_L, Socky.SPR_H, 6, 400)
        self.cycle = self.idle_right_cycle
        self.cycle.start()

        self.keys_held = 0

    def update_pos(self):
        """update the players position"""
        (x_pos, y_pos) = self.pos
        (x_vel, y_vel) = self.vel
        x_pos += x_vel
        y_pos += y_vel

        self.pos = (x_pos, y_pos)

    def update(self):
        """update the player bearing, velocity and position"""
        self.update_pos()

    def render(self):
        """render the player model and return the surface and position on screen where it should be rendered"""
        return self.cycle.get_frame(), self.pos

    def __repr__(self):
        """string representation of the player for debugging"""
        (x_pos, y_pos) = self.pos
        (x_vel, y_vel) = self.vel

        return (
            "position: ({x_pos:.2f}, {y_pos:.2f}), "
            "velocity: ({x_vel:.2f}, {y_vel:.2f}), "
        ).format(
            x_pos=x_pos, y_pos=y_pos, x_vel=x_vel, y_vel=y_vel
        )

    def handle_keydown(self, event):
        """handle when player presses a key"""
        if event.key == LEFT_KEY:
            self.facing = FACING_LEFT
            self.cycle = self.walk_left_cycle
            self.cycle.start()
            self.vel = (-Socky.MOVE_SPEED, 0)
            self.keys_held += 1
        elif event.key == RIGHT_KEY:
            self.facing = FACING_RIGHT
            self.cycle = self.walk_right_cycle
            self.cycle.start()
            self.vel = (Socky.MOVE_SPEED, 0)
            self.keys_held += 1
        elif event.key == UP_KEY:
            self.vel = (0, -Socky.MOVE_SPEED)
            self.keys_held += 1
        elif event.key == DOWN_KEY:
            self.vel = (0, Socky.MOVE_SPEED)
            self.keys_held += 1

    def handle_keyup(self, event):
        """handle when player releases a key"""
        if (event.key == LEFT_KEY or event.key == RIGHT_KEY
                or event.key == UP_KEY or event.key == DOWN_KEY):
            self.keys_held -= 1

            if self.keys_held == 0:
                self.vel = (0, 0)
                if self.facing == FACING_LEFT:
                    self.cycle = self.idle_left_cycle
                if self.facing == FACING_RIGHT:
                    self.cycle = self.idle_right_cycle
                self.cycle.start()
