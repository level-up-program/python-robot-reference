from typing import Callable
from levelup.controller import GameController, Direction


class GameUI:

    game: GameController

    def __init__(self):
        self.game = GameController()

    def prompt(self, message: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{message}\n> ")
            if validation_fn(response):
                break
        return response

    def start(self):
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.game.create_character(character)
        valid_directions = [x.value for x in Direction]
        while True:
            responce = self.prompt(
                f"Where would you like to go? {valid_directions}\n(or ctrl+c to quit)",
                lambda x: x in valid_directions,
            )
            self.game.move(Direction(responce))
