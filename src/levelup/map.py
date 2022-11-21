from enum import Enum
from typing import Tuple, List
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
    positions: List[Position]

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        self.positions = []
        for x in [i for i in range(0, self.size[0])]:
            for y in [i for i in range(0, self.size[1])]:
                self.positions.append(Position(x, y))
        self.position_count = (x + 1) * (y + 1)

    def is_valid_position(self, position: Position) -> bool:
        return position in self.positions

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        x, y = starting_position.coordinates
        if direction is Direction.NORTH:
            y += 1
        elif direction is Direction.SOUTH:
            y -= 1
        elif direction is Direction.EAST:
            x += 1
        elif direction is Direction.WEST:
            x -= 1
        return Position(x, y)
