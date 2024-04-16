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

    def test_Multiplication(self):
	a = 2
	b = 3
	c = 4
	multiplication = Arithmetic.Multiplication(a, b, c)
	assert multiplication == 24

    def test_Division(self):
	a = 10
	b = 2
	c = 5
	division = Arithmetic.Division(a, b, c)
	assert division == 1

if __name__ == '__main__':
    unittest.main()
