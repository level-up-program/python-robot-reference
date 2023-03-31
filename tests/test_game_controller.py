from unittest import TestCase
from levelup.controller import GameController
from fake_character import FakeCharacter
from levelup.direction import Direction

class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        assert testobj.status != None

    def test_create_character_updates_status(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        testobj.create_character(arbitrary_name)
        self.assertEqual(arbitrary_name, testobj.status.character_name)
        self.assertIsNotNone(testobj.character)

    def test_start_game_creates_map_and_enters_char(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        fake_char = FakeCharacter(arbitrary_name)
        testobj.character = fake_char

        testobj.start_game()
        
        self.assertIsNotNone(testobj.map)
        self.assertTrue(fake_char.is_enter_map_called)
        self.assertTrue(testobj.status.running)
        self.assertEqual(0, testobj.status.move_count)

    def test_move_calls_char_move(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        fake_char = FakeCharacter(arbitrary_name)
        testobj.character = fake_char
        arbitrary_direction = Direction.NORTH

        testobj.move(arbitrary_direction)

        self.assertTrue(fake_char.is_move_called)
        self.assertEqual(fake_char.last_move_direction, arbitrary_direction)
        
        
