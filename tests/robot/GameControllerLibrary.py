from levelup.controller import GameController


class GameControllerLibrary:
    def initialize_controller(self):
        self.controller = GameController()

    def create_character_with_name(self, charactername):
        self.controller.create_character(charactername)
        self.controller.start_game()

    def character_name_should_be(self, expected):
        if self.controller.character.name != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.character.name, expected)
            )

    def number_of_map_positions_should_be(self, expected):
        if self.controller.map.position_count != int(expected):
            raise AssertionError(
                "%s != %s" % (self.controller.map.position_count, expected)
            )

    def starting_X_coordinate_should_be(self, expected):
        if self.controller.status.current_position.coordinates[0] != int(expected):
            raise AssertionError(
                "%s != %s"
                % (self.controller.status.current_position.coordinates[0], expected)
            )

    def starting_Y_coordinate_should_be(self, expected):
        if self.controller.status.current_position.coordinates[1] != int(expected):
            raise AssertionError(
                "%s != %s"
                % (self.controller.status.current_position.coordinates[1], expected)
            )

    def starting_move_count_should_be(self, expected):
        assert self.controller.status.move_count == int(expected)
