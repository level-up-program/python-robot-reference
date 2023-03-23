from levelup.controller import GameController
from levelup.controller import Direction
from levelup.position import Position
from levelup.map import Direction, GameMap


class MoveLibrary:
    start_x: int
    start_y: int

    def initialize_character_xposition_with(self, x_position):
        pass

    def initialize_character_yposition_with(self, y_position):
        pass

    def initialize_character_moveCount_with(self, move_count):
        pass

    def move_in_direction(self, direction):
        pass

    def character_xposition_should_be(self, expected):
        raise AssertionError("Not implemented")

    def character_yposition_should_be(self, expected):
        raise AssertionError("Not implemented")

    def character_moveCount_should_be(self, expected):
        raise AssertionError("Not implemented")
