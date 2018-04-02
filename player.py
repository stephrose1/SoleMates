
LEFT_KEY = 97
RIGHT_KEY = 100
UP_KEY = 119
DOWN_KEY = 115


class Player:
    # how much the player moves per tick
    MOVE_SPEED = 6

    def __init__(self, spritesheet):
        """Set up initial state of the player"""
        # current position of the player
        self.pos = (50, 50)

        # current velocity of the player, as a vector
        self.vel = (0, 0)

        # load spritesheet
        (self.up_sprite,
         self.right_sprite,
         self.down_sprite,
         self.left_sprite) = spritesheet.load_strip((0, 0, 100, 100), 4)

        # set render sprite
        self.sprite = self.right_sprite

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
        return self.sprite, self.pos

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
            self.sprite = self.left_sprite
            self.vel = (-Player.MOVE_SPEED, 0)
        elif event.key == RIGHT_KEY:
            self.sprite = self.right_sprite
            self.vel = (Player.MOVE_SPEED, 0)
        elif event.key == UP_KEY:
            self.sprite = self.up_sprite
            self.vel = (0, -Player.MOVE_SPEED)
        elif event.key == DOWN_KEY:
            self.sprite = self.down_sprite
            self.vel = (0, Player.MOVE_SPEED)

    def handle_keyup(self, event):
        """handle when player releases a key"""
        if event.key == LEFT_KEY or event.key == RIGHT_KEY:
            self.vel = (0, 0)
        if event.key == UP_KEY or event.key == DOWN_KEY:
            self.vel = (0, 0)
