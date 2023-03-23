from levelup.controller import GameController
from levelup.controller import Direction
from levelup.position import Position
from levelup.map import Direction, GameMap


class MoveLibrary:
    start_x: int
    start_y: int

    def initialize_character_xposition_with(self, x_position):
        self.start_x = int(x_position)

    def initialize_character_yposition_with(self, y_position):
        self.start_y = int(y_position)

    def initialize_character_moveCount_with(self, move_count):
        self.move_count = int(move_count)

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.create_character("")
        self.controller.start_game()
        self.controller.set_character_position(Position(self.start_x, self.start_y))
        self.controller.status.move_count = self.move_count
        new_direction = Direction[direction]
        self.controller.move(new_direction)

    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.current_position.coordinates[0]
        if end_x != int(expected):
            raise AssertionError(f"x{end_x} != x{expected}")

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position.coordinates[1]
        if end_y != int(expected):
            raise AssertionError(f"y{end_y} != y{expected}")

    def character_moveCount_should_be(self, expected):
        move_count = self.controller.status.move_count
        if move_count != int(expected):
            raise AssertionError(f"{move_count} != {expected}")
