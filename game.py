from menu import Menu
import pygame

MENU_MODE = 0


class Store:
    def __init__(self):
        self.level_select_disabled = True


class Game:
    def __init__(self, screen):
        self._ev_handlers = dict()
        self._renderer_funcs = []
        self._screen = screen
        self.store = Store()

    def register_ev_handler(self, callback, event_type):
        """
        ** event subscription **
        call this function to subscribe to an event
        """
        if not (event_type in self._ev_handlers):
            self._ev_handlers[event_type] = []

        self._ev_handlers[event_type].append(callback)

    def handle_event(self, event):
        """
        ** event dispatch **
        when the game receives an event it calls all registered event handlers
        """
        if event.type in self._ev_handlers:
            for callback in self._ev_handlers[event.type]:
                callback(event)

    def register_render_func(self, callback):
        """
        ** render subscription **
        when register your function to draw things to the screen here
        the callback receives the screen to render onto
        """
        self._renderer_funcs.append(callback)

    def _render(self):
        """
        ** render dispatch **
        the game calls all the registered render functions
        """
        self._screen.fill((0, 0, 0))

        for render_func in self._renderer_funcs:
            render_func(self._screen)

        pygame.display.flip()

    def set_mode(self, game_mode):
        self._renderer_funcs = []
        self._ev_handlers = dict()

        if game_mode == MENU_MODE:
            Menu(self, self._screen.get_rect())

    def tick(self):
        self._render()
