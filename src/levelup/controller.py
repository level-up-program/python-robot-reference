import logging
from dataclasses import dataclass
from levelup.character import Character, DEFAULT_CHARACTER_NAME
from levelup.map import Direction, DEFAULT_MAP_ENTRY_POINT, GameMap
from levelup.position import Position

ARBITRARY_INVALID_INITIALIZED_POSITION = Position(-1, -1)


@dataclass
class GameStatus:
    move_count: int = 0
    current_position: Position = ARBITRARY_INVALID_INITIALIZED_POSITION

    def __str__(self):
        return f"Moved {self.move_count} times, currently on position {self.current_position}"


class GameController:
    status: GameStatus
    character: Character

    def __init__(self):
        self.status = GameStatus()
        self.map = GameMap()

    def start_game(self):
        self.character.enter_map(self.map)
        self.set_character_position(self.map.default_entry_point)

    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.move_count += 1
        self.status.current_position = self.character.position

    def set_character_position(self, position: Position):
        self.character.position = position

    def get_total_positions(self):
        pass
