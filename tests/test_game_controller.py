from unittest import TestCase
from levelup.controller import GameController, ARBITRARY_INVALID_INITIALIZED_POSITION
from levelup.character import DEFAULT_CHARACTER_NAME


class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            ARBITRARY_INVALID_INITIALIZED_POSITION,
        )

    def test_create_default_character(self):
        testobj = GameController()
        testobj.create_character("")
        self.assertEqual(DEFAULT_CHARACTER_NAME, testobj.character.name)

    def test_create_character(self):
        testobj = GameController()
        expected_character_name = "ArbitraryName"
        testobj.create_character(expected_character_name)
        self.assertEqual(expected_character_name, testobj.character.name)
