from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.map import Map

class TestMap(TestCase):
    
    def test_init(self):
        testobj = Map()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))
        self.assertEqual(3, testobj.positions[3][0].x)
        self.assertEqual(0, testobj.positions[3][0].y)
