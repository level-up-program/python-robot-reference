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
