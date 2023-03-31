from levelup.position import Position
from typing import Tuple
from levelup.controller import Direction, InvalidMoveException

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        temp_pos = []
        for x in range(self.size[0]):
            y_range = []
            for y in range(self.size[1]):
                new_pos = Position(x,y)
                y_range.append(new_pos)
            temp_pos.append(y_range)
        self.positions = temp_pos

    def is_position_valid(self, position :Position):
        if position.x > 0 and position.x < self.size[0] and position.y > 0 and position.y < self.size[1]:
            return True
        else:
            return False

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        if direction == Direction.NORTH:
            return Position(current_position.x, current_position.y + 1)
        elif direction == Direction.SOUTH:
            return Position(current_position.x, current_position.y - 1)
        elif direction == Direction.EAST:
            return Position(current_position.x + 1, current_position.y)
        elif direction == Direction.WEST:
            return Position(current_position.x - 1, current_position.y)
        else:
            raise InvalidMoveException()
