from menu import Menu
import pygame

MENU_STATE = 0


class Game:
    def __init__(self, screen):
        self._ev_handlers = dict()
        self._renderer_funcs = []
        self._screen = screen

    def register_ev_handler(self, callback, event_type):
        if not (event_type in self._ev_handlers):
            self._ev_handlers[event_type] = []

        self._ev_handlers[event_type].append(callback)

    def register_render_func(self, callback):
        self._renderer_funcs.append(callback)

    def _render(self):
        self._screen.fill((0, 0, 0))

        for render_func in self._renderer_funcs:
            render_func(self._screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type in self._ev_handlers:
            for callback in self._ev_handlers[event.type]:
                callback(event)

    def set_state(self, game_state):
        self._renderer_funcs = []
        self._ev_handlers = dict()

        if game_state == MENU_STATE:
            Menu(self, self._screen.get_rect())

    def tick(self):
        self._render()
