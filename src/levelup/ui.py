import logging
from typing import Callable
from levelup.controller import GameController, Direction

VALID_DIRECTIONS = [x.value for x in Direction]
VALID_COMMANDS = [x.value for x in Direction] + ['q']


class GameApp:
    controller: GameController

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
        return response

    def create_character(self):
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.controller.create_character(character)

    def move_loop(self):
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or q to quit)",
                lambda x: x in VALID_COMMANDS,
            )
            if response == 'q':
                self.quit()
            direction = Direction(response)
            self.controller.move(direction)
            print(self.controller.status)

    def start(self):
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def quit(self):
        print(f"\n\n{self.controller.status}")
        quit()
