from unittest import TestCase
from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    
    def test_init_creates_positions(self):
        testobj = Map()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))

    def test_init_creates_positions_with_crrect_x_y(self):
        testobj = Map()
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

    def test_calculate_new_position_when_valid_NORTH(self):
        testobj = Map()
        startingPosition = Position(0,0)
        expectedPosition = Position(0,1)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.NORTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_SOUTH(self):
        testobj = Map()
        startingPosition = Position(3, 3)
        expectedPosition = Position(3, 2)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.SOUTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_EAST(self):
        testobj = Map()
        startingPosition = Position(3, 3)
        expectedPosition = Position(4, 3)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.EAST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_WEST(self):
        testobj = Map()
        startingPosition = Position(3, 3)
        expectedPosition = Position(2, 3)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.WEST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_invalid_NORTH(self):
        testobj = Map()
        startingPosition = Position(9, 9)
        expectedPosition = Position(9, 9)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.NORTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_invalid_SOUTH(self):
        testobj = Map()
        startingPosition = Position(0, 0)
        expectedPosition = Position(0, 0)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.SOUTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_EAST(self):
        testobj = Map()
        startingPosition = Position(9, 9)
        expectedPosition = Position(9, 9)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.EAST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_WEST(self):
        testobj = Map()
        startingPosition = Position(0, 0)
        expectedPosition = Position(0, 0)
        actualPosition = testobj.calculate_new_position(
            startingPosition, Direction.WEST)
        self.assertEqual(expectedPosition, actualPosition)
