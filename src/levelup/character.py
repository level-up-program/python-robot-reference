from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_POSITION = Position(0, 0)
DEFAULT_CHARACTER_NAME = "Character"


class Character:
    name: str
    position: Position = DEFAULT_POSITION

    def __init__(self, name: str):
        self.name = name or DEFAULT_CHARACTER_NAME

    def enter_map(self, game_map: GameMap):
        self.map = game_map

    def move(self, direction: Direction):
        pass
