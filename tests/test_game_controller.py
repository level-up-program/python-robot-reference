from unittest import TestCase
from levelup.controller import GameController, DEFAULT_PLAYER_NAME


class TestGameController(TestCase):
    def test_init(self):
        test_controller = GameController()
        self.assertEqual(DEFAULT_PLAYER_NAME, test_controller.status.player.name)

    def test_create_default_player(self):
        test_controller = GameController()
        test_controller.create_player("")
        self.assertEqual(DEFAULT_PLAYER_NAME, test_controller.status.player.name)

    def test_create_player(self):
        test_controller = GameController()
        expected_player_name = "ArbitraryName"
        test_controller.create_player(expected_player_name)
        self.assertEqual(expected_player_name, test_controller.status.player.name)
