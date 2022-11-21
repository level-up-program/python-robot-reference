from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from levelup.position import Position


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_enter_map(self):
        testmap = GameMap()

        testobj = Character("")
        self.assertEqual(testobj.map, None)

        testobj.enter_map(testmap)
        self.assertNotEqual(testobj.map, None)
        self.assertEqual(testobj.position, testmap.starting_position)

    def test_valid_moves(self):
        testobj = Character("")
        testobj.enter_map(GameMap())

        testobj.position = Position(0, 0)
        testobj.move(Direction.NORTH)
        expected_position = Position(0, 1)
        self.assertEqual(str(testobj.position), str(expected_position))

        testobj.position = Position(0, 1)
        testobj.move(Direction.SOUTH)
        expected_position = Position(0, 0)
        self.assertEqual(str(testobj.position), str(expected_position))

        testobj.position = Position(0, 0)
        testobj.move(Direction.EAST)
        expected_position = Position(1, 0)
        self.assertEqual(str(testobj.position), str(expected_position))

        testobj.position = Position(1, 0)
        testobj.move(Direction.WEST)
        expected_position = Position(0, 0)
        self.assertEqual(str(testobj.position), str(expected_position))

    def test_invalid_moves(self):
        testobj = Character("")
        testobj.enter_map(GameMap())

        testobj.position = Position(0, 0)

        with self.assertRaises(InvalidMoveException):
            testobj.move(Direction.SOUTH)
        expected_position = Position(0, 0)
        self.assertEqual(testobj.position, expected_position)

        with self.assertRaises(InvalidMoveException):
            testobj.move(Direction.WEST)
        expected_position = Position(0, 0)
        self.assertEqual(str(testobj.position), str(expected_position))

        testobj.position = Position(9, 9)

        with self.assertRaises(InvalidMoveException):
            testobj.move(Direction.NORTH)
        expected_position = Position(9, 9)
        self.assertEqual(str(testobj.position), str(expected_position))

        with self.assertRaises(InvalidMoveException):
            testobj.move(Direction.EAST)
        expected_position = Position(9, 9)
        self.assertEqual(str(testobj.position), str(expected_position))
