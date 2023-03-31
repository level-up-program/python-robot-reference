from levelup.position import Position
from typing import Tuple
from levelup.controller import Direction

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        temp_pos = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                new_pos = Position(0,0)
                temp_pos.append(new_pos)
        self.positions = temp_pos

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        return None