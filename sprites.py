import pygame
from settings import *
vec = pygame.math.Vector2


class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.neutral_frames[0]

        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def load_images(self):
        self.neutral_frames = [self.game.player_spritesheet.get_image(60, 0, 32, 32),
                               self.game.player_spritesheet.get_image(60, 33, 32, 31)]
        for frame in self.neutral_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [self.game.player_spritesheet.get_image(0, 33, 59, 32),
                              self.game.player_spritesheet.get_image(0, 66, 59, 32),
                              self.game.player_spritesheet.get_image(0, 0, 59, 32),
                              self.game.player_spritesheet.get_image(0, 66, 59, 32)]
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))


    def get_keys(self):
        self.vel = vec(0, 0)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def collide_with_obstacles(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.obstacles, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.obstacles, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.animate()
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_obstacles('x')
        self.rect.y = self.pos.y
        self.collide_with_obstacles('y')

    def animate(self):
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if not self.walking:
            if now - self.last_update > 600:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.neutral_frames)
                bottom = self.rect.bottom
                self.image = self.neutral_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom


class Clothes(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.attacking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.neutral_frames[0]

        self.rect = self.image.get_rect()
        self.pos = vec(x, y)

    def load_images(self):
        self.neutral_frames = [self.game.clothes_spritesheet.get_image(0, 0, 134, 86)]
        for frame in self.neutral_frames:
            frame.set_colorkey(BLACK)
        self.attacking_frames = [self.game.clothes_spritesheet.get_image(0, 190, 213, 87),
                                 self.game.clothes_spritesheet.get_image(163, 0, 137, 121),
                                 self.game.clothes_spritesheet.get_image(0, 87, 162, 121)]

    def update(self):
        self.animate()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def animate(self):
        now = pygame.time.get_ticks()
        if not self.attacking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.neutral_frames)


class Spider(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.spider_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)

    def update(self):
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Robot(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.attacking = True
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.frames[0]

        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def load_images(self):
        self.frames = [self.game.robot_spritesheet.get_image(248, 0, 123, 208),
                       self.game.robot_spritesheet.get_image(0, 209, 123, 208),
                       self.game.robot_spritesheet.get_image(124, 209, 123, 208),
                       self.game.robot_spritesheet.get_image(0, 209, 123, 208),
                       self.game.robot_spritesheet.get_image(248, 0, 123, 208),
                       self.game.robot_spritesheet.get_image(0, 0, 123, 208),
                       self.game.robot_spritesheet.get_image(124, 0, 123, 208),
                       self.game.robot_spritesheet.get_image(0, 0, 123, 208)]

        for frame in self.frames:
            frame.set_colorkey(BLACK)

    def animate(self):
        now = pygame.time.get_ticks()
        if self.attacking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                self.rect = self.image.get_rect()



    def update(self):
        self.animate()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class Vacuum(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.vacuum_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Item(pygame.sprite.Sprite):
    def __init__(self, game, pos, type,):
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.center = pos
