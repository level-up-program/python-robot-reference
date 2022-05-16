from levelup.game_controller import GameController


class GameControllerLibrary:
    def initialize_controller(self):
        self.controller = GameController()

    def create_player_with_name(self, playername):
        self.controller.create_player(playername)

    def player_name_should_be(self, expected):
        if self.controller.status.player.name != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.player.name, expected)
            )
