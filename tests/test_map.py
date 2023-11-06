from unittest import TestCase
from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    
    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_init_creates_positions(self):
    #     testobj = Map()
    #     self.assertNotEqual(None, testobj.positions)
    #     self.assertEqual(10, len(testobj.positions))

    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_init_creates_positions_with_correct_x_y(self):
    #     testobj = Map()
    #     self.assertEqual(3, testobj.positions[3][0].x)
    #     self.assertEqual(7, testobj.positions[3][7].y)

    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_is_position_valid_when_true(self):
    #     testobj = Map()
    #     self.assertTrue(testobj.is_position_valid(Position(3,4)))

    # Given the example above, what should these test?
    def test_is_position_valid_when_x_too_small(self):
        # TODO: Put code here
        pass

    def test_is_position_valid_when_x_too_big(self):
        # TODO: Put code here
        pass

    def test_is_position_valid_when_y_too_small(self):
        # TODO: Put code here
        pass

    def test_is_position_valid_when_y_too_big(self):
        # TODO: Put code here
        pass

    def test_is_position_valid_when_x_and_y_too_big(self):
        # TODO: Put code here
        pass

    # # Remove comments to run this test, which will motivate you to write the production method
    # def test_calculate_new_position_when_valid_NORTH(self):
    #     testobj = Map()
    #     startingPosition = Position(0,0)
    #     expectedPosition = Position(0,1)
    #     actualPosition = testobj.calculate_new_position(startingPosition, Direction.NORTH)
    #     self.assertEqual(expectedPosition, actualPosition)

    # Given the example above, what should these test?
    def test_calculate_new_position_when_valid_SOUTH(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_valid_EAST(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_valid_WEST(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_invalid_NORTH(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_invalid_SOUTH(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_valid_EAST(self):
        # TODO: Put code here
        pass

    def test_calculate_new_position_when_valid_WEST(self):
        # TODO: Put code here
        pass 
