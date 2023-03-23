from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.map import Direction
from levelup.position import Position


class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            None,
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

    def test_start_game(self):
        testobj = GameController()
        testobj.create_character("")
        self.assertIsNone(testobj.character.position)
        self.assertIsNone(testobj.character.map)
        testobj.start_game()
        self.assertEqual(testobj.map.starting_position, testobj.character.position)
        self.assertEqual(testobj.map, testobj.character.map)

    def test_set_character_position(self):
        testobj = GameController()
        testobj.create_character("")
        testobj.start_game()
        expected_position = Position(1, 1)
        self.assertNotEqual(expected_position, testobj.character.position)
        testobj.set_character_position(expected_position)
        self.assertEqual(expected_position, testobj.character.position)

    def test_get_total_positions(self):
        testobj = GameController()
        expected_position_count = testobj.map.position_count
        actual_position_count = testobj.get_total_positions()
        self.assertEqual(expected_position_count, actual_position_count)

    def test_valid_move(self):
        testobj = GameController()
        testobj.create_character("")
        testobj.start_game()
        self.assertEqual(testobj.status.move_count, 0)

        testobj.character.move = MagicMock(return_value=None)
        direction_to_move = Direction.NORTH
        testobj.move(direction_to_move)
        testobj.character.move.assert_called_with(direction_to_move)
        self.assertEqual(testobj.status.move_count, 1)

    def test_invalid_move(self):
        testobj = GameController()
        fake_character = create_autospec(Character(""))
        testobj.character = fake_character
        testobj.character.move.side_effect = InvalidMoveException("BOOM!")

        self.assertEqual(testobj.status.move_count, 0)
