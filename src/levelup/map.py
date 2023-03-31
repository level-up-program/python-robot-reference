from levelup.position import Position
from levelup.controller import Direction

class Map ():

    starting_position = Position(0,0)

    def __init__(self):
        pass

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        return None