from calculator import Calculator


class CalculatorLibrary:
    """
    Test library for testing *Calculator* business logic.
    """

    def __init__(self):
        self._calc = Calculator()
        self._buffer = []
        self._result = None

    def clear(self):
        self._buffer = []

    def enters_values(self, value):
        for item in value.split(','):
            self._buffer.append(int(item))

    def add(self, *args):
        integers = [int(i) for i in self._buffer]
        # import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self._result = self._calc.add(*integers)

    def result_should_be(self, expected):
        if int(self._result) != int(expected):
            raise AssertionError('%s != %s' % (self._result, expected))
