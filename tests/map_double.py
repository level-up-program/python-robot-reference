from levelup.map import Map
from levelup.position import Position
from levelup.direction import Direction

class MapDouble (Map):

    STUBBED_X = 3
    STUBBED_Y = 4

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        return Position(self.STUBBED_X, self.STUBBED_Y)
