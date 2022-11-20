import logging
from typing import Callable
from levelup.controller import GameController
from levelup.map import Direction

VALID_DIRECTIONS = [x.value for x in Direction]


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

    def start(self):
        self.create_character()
        self.controller.start_game()
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or ctrl+c to quit)",
                lambda x: x in VALID_DIRECTIONS,
            )
            self.controller.move(Direction(response))
            print(f"You are now on position {self.controller.character.position}")

    def quit(self):
        logging.info("Calling quit from App")
