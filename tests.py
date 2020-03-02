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
        expected = 0
        self.assertEqual(expected, actual)

    def test3(self):
        list = []
        list = [4, 8, 2, 0, 1, 9]
        self.assertEqual([4, 9], task.getFirstAndLast(list))

    def test4(self):
        dayDiff = task.getNumDays("Monday", "Tuesday")
        self.assertEqual(1, dayDiff)
        dayDiff = task.getNumDays("Tuesday", "Monday")
        self.assertEqual(1, dayDiff)


if __name__ == '__main__':
    unittest.main()
