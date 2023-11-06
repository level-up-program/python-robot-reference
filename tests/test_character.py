from unittest import TestCase
from levelup.character import Character, DEFAULT_CHARACTER_NAME
from tests.map_double import MapDouble
from levelup.direction import Direction

class TestCharacter(TestCase):
    ARBITRARY_NAME = "MyName"

    def test_init(self):
        testobj = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobj.name)

    def test_init_when_empty(self):
        testobj = Character("  ")
        self.assertEqual(DEFAULT_CHARACTER_NAME, testobj.name)

    def test_enter_map_sets_map_and_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = MapDouble()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.map)
        self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    def test_move_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = MapDouble()
        testobj.map = stubbed_map
        
        testobj.move(Direction.EAST)

        self.assertEqual(stubbed_map.STUBBED_X, testobj.current_position.x)
        self.assertEqual(stubbed_map.STUBBED_Y, testobj.current_position.y)

