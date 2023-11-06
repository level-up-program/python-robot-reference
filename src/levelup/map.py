from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        # TODO: implement method here and remove the print statement below
        print("map constructor method not yet implemented")

    def is_position_valid(self, position :Position) -> bool:
        # TODO: implement method here and remove the print statement below
        print("is_position_valid method not yet implemented")
        return False        

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        # TODO: implement method here and remove the print statement below
        print("calculate_new_position method not yet implemented")
        return None
