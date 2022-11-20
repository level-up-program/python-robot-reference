from enum import Enum
from typing import Tuple
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(0, 0)
    size: Tuple[int, int] = (10, 10)
    position_count: int

    def __init__(self):
        self.create_positions()

    def create_positions(self):
        self.positions = []
        for y in [i for i in range(0, self.size[0])]:
            for x in [i for i in range(0, self.size[1])]:
                self.positions.append([Position(x, y)])
        self.position_count = (x + 1) * (y + 1)
