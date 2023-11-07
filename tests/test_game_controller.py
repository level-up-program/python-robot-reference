from unittest import TestCase
from levelup.controller import GameController
from tests.character_double import CharacterDouble
from levelup.direction import Direction

class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        assert testobj.status != None

    # Remove comments to run this test, which will motivate you to write the production method
    # def test_create_character_updates_status(self):
    #     testobj = GameController()
    #     arbitrary_name = "ARBITRARY"
    #     testobj.create_character(arbitrary_name)
    #     self.assertEqual(arbitrary_name, testobj.status.character_name)
    #     self.assertIsNotNone(testobj.character)

    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_start_game_creates_map_and_enters_char(self):
    #     testobj = GameController()
    #     arbitrary_name = "ARBITRARY"
    #     mock_char = CharacterDouble(arbitrary_name)
    #     testobj.character = mock_char

    #     testobj.start_game()
        
    #     self.assertIsNotNone(testobj.map)
    #     self.assertTrue(mock_char.is_enter_map_called)
    #     self.assertEqual(0, testobj.status.move_count)

    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_move_calls_char_move(self):
    #     testobj = GameController()
    #     arbitrary_name = "ARBITRARY"
    #     mock_char = CharacterDouble(arbitrary_name)
    #     testobj.character = mock_char
    #     arbitrary_direction = Direction.NORTH

    #     testobj.move(arbitrary_direction)

    #     self.assertTrue(mock_char.is_move_called)
    #     self.assertEqual(mock_char.last_move_direction, arbitrary_direction)
        
        
