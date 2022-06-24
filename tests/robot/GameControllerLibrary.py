from levelup.controller import GameController


class GameControllerLibrary:
    def initialize_controller(self):
        self.controller = GameController()

    def create_character_with_name(self, charactername):
        self.controller.create_character(charactername)

    def character_name_should_be(self, expected):
        if self.controller.status.character.name != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.character.name, expected)
            )
