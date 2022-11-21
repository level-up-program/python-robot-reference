from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_CHARACTER_NAME = "Character"


class InvalidMoveException(Exception):
    pass


class Character:
    name: str
    map: GameMap = None
    position: Position = None

    def __init__(self, name: str):
        self.name = name or DEFAULT_CHARACTER_NAME

    def enter_map(self, game_map: GameMap):
        self.map = game_map
        self.position = self.map.starting_position

    def move(self, direction: Direction):
        next_position = self.map.calculate_position(self.position, direction)
        if self.map.is_valid_position(next_position):
            self.position = next_position
        else:
            raise InvalidMoveException(f"You cannot move to position {next_position}")
