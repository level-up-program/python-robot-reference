from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    
    def test_init_creates_positions(self):
        testobj = Map()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))
        self.assertEqual(3, testobj.positions[3][0].x)
        self.assertEqual(7, testobj.positions[3][7].y)

    def test_is_position_valid_when_true(self):
        testobj = Map()
        self.assertTrue(testobj.is_position_valid(Position(3,4)))

    def test_is_position_valid_when_x_too_small(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(-1, 4)))

    def test_is_position_valid_when_x_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(10, 4)))

    def test_is_position_valid_when_y_too_small(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(0, -1)))

    def test_is_position_valid_when_y_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(3, 10)))

    def test_is_position_valid_when_x_and_y_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(11, 10)))

    
