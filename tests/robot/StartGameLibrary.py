from levelup.controller import GameController
from robot.libraries.BuiltIn import BuiltIn

class StartGameLibrary:
    ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

    def initialize_controller(self):
        self.controller = GameController()

    def number_of_map_positions_should_be(self, expected):
        actual = self.controller.get_total_positions()
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def starting_X_coordinate_should_be(self, expected):
        actual = self.controller.status.current_position[0]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def starting_Y_coordinate_should_be(self, expected):
        actual = self.controller.status.current_position[0]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def starting_move_count_should_be(self, expected):
        actual = self.controller.status.move_count
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"
