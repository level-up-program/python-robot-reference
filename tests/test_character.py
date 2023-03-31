from unittest import TestCase
from levelup.character import Character
from fake_map import FakeMap
from levelup.controller import Direction

class TestCharacter(TestCase):
    ARBITRARY_NAME = "MyName"

    def test_init(self):
        testobj = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobj.name)

    def test_enter_map_sets_map_and_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.map)
        self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    def test_move_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = FakeMap()
        testobj.map = stubbed_map
        
        testobj.move(Direction.EAST)

        self.assertEqual(stubbed_map.STUBBED_X, testobj.current_position.x)
        self.assertEqual(stubbed_map.STUBBED_Y, testobj.current_position.y)

