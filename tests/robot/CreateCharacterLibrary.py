from levelup.controller import GameController

class CreateCharacterLibrary:
    character_name_input = ""

    def provide_character_name(self, character_name_input):
        self.character_name_input = character_name_input

    def create_the_character(self):
        self.controller = GameController()
        self.controller.create_character(character_name=self.character_name_input)

    def character_name_is(self, expected):
        actual = self.controller.status.character_name
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"