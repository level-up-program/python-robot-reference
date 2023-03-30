from levelup.controller import GameController
from levelup.controller import Direction

class MoveLibrary:
    start_x: int
    start_y: int

    controller = GameController()

    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_movecount_with(self, move_count):
        self.controller.set_current_move_count(move_count)

    def move_in_direction(self, direction):
        self.controller.set_character_position((self.start_x, self.start_y))
        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.current_position[0]
        assert end_x == expected, f"Expected: {expected}, Actual: {end_x}"

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position[1]
        assert end_y == expected, f"Expected: {expected}, Actual: {end_y}"

    def character_movecount_should_be(self, expected):
        actual = self.controller.status.move_count
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"
