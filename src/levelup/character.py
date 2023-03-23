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
        pass

    def move(self, direction: Direction):
        pass
