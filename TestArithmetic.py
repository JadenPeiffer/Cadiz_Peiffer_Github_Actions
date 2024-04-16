import unittest
import Arithmetic


class MyTestCase(unittest.TestCase):

    def test_Addition(self):
        a = 1
        b = 2
        c = 3
        addition = Arithmetic.Addition(a, b, c)
        assert addition == 6

    def test_Subtraction(self):
        a = 1
        b = 2
        c = 3
        subtraction = Arithmetic.Subtraction(a, b, c)
        assert subtraction == -4


if __name__ == '__main__':
    unittest.main()
