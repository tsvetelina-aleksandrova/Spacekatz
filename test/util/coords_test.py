import unittest
import mock
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))

from backend.util.coords import Coords


class CoordsTest(unittest.TestCase):
    def test_set(self):
        test_x, test_y, test_z = (1, 2, 3)
        test_coords = Coords(test_x, test_y)
        self.assertEqual(test_coords.x, test_x)
        self.assertEqual(test_coords.y, test_y)
        test_coords.x = test_z
        self.assertEqual(test_coords.x, test_z)

    def test_set_err(self):
        test_value = 1.2
        with self.assertRaises(ValueError):
            test_coords = Coords(test_value, test_value)
        test_coords = Coords(0, 0)
        with self.assertRaises(ValueError):
            test_coords.x = test_value


if __name__ == '__main__':
    unittest.main()
