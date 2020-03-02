import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        actual = task.getArea(3)
        expected = 3 * 3 * math.pi
        self.assertEqual(expected, actual)

    def test2(self):
        actual = task.getArea(0)
        expected = 0.0
        self.assertNotEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
