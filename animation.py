import pygame


class Animation:
    def __init__(self, frames, duration):
        self.frames = frames
        self.frame_duration = duration / len(frames)
        self.start_time = 0
        self.stop_time = 0
        self.playing = False
        self.frame_index = 0

    def get_frame(self):
        if self.playing:
            ticks = pygame.time.get_ticks() - self.start_time
        else:
            ticks = self.stop_time - self.start_time
        return self.frames[int((ticks / self.frame_duration) % len(self.frames))]

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.playing = True

    def stop(self):
        self.stop_time = pygame.time.get_ticks()
        self.playing = False
        pass
