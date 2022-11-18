from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_POSITION = Position(0, 0)


class Character:
    name: str
    current_position: Position = DEFAULT_POSITION

    def __init__(self, name: str):
        self.name = name

    def enter_map(self, game_map: GameMap):
        pass

    def move(self):
        pass
