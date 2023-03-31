from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.map import Map

class TestMap(TestCase):
    
    def test_init(self):
        testobj = Map()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(100, len(testobj.positions))
