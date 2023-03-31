from unittest import TestCase
from levelup.position import Position


class TestPositionInitWithXY(TestCase):
    def test_init(self):
        ARBITRARY_X = 3
        ARBITRARY_Y = 4
        testobj = Position(3,4)
        self.assertEqual(ARBITRARY_X, testobj.x)
        self.assertEqual(ARBITRARY_Y, testobj.y)
