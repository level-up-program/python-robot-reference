from levelup.map import Map
from levelup.character import Character
from levelup.controller import Direction

class FakeCharacter (Character):

    is_move_called = False
    is_enter_map_called = False
    last_move_direction = None

    def move(self, direction: Direction) -> None:
        self.is_move_called = True
        self.last_move_direction = direction

    def enter_map(self, map: Map) -> None:
        self.is_enter_map_called = True
