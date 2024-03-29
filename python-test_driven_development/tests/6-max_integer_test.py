#!/usr/bin/python3
import unittest


class TestMaxInteger(unittest.TestCase):
    
    def test_max_integer(self):
        max_integer = __import__("6-max_integer").max_integer
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1**2, 200, -30, 2000/2]), 1000)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([200, 1, 2]), 200)
        self.assertEqual(max_integer([1, 2, 20, 4, 5]), 20)
        with self.assertRaises(TypeError):
            max_integer(1)

if __name__ == '__main__':
    unittest.main()
