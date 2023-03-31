from levelup.map import Map
from levelup.character import Character
from levelup.controller import Direction

class FakeCharacter (Character):

    is_move_called = False

    def move(self, direction: Direction) -> None:
        self.is_move_called = True
