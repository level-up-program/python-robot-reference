from unittest import TestCase
import calculator

TEST_NUMBER_1 = 50
TEST_NUMBER_2 = 70


class TestCalculator(TestCase):
    def test_add(self):
        calc = calculator.Calculator()
        expected_sum = 120
        actual_sum = calc.add(TEST_NUMBER_1, TEST_NUMBER_2)
        self.assertEqual(expected_sum, actual_sum)
