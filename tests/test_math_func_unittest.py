import unittest
import math_func


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_func.add_func(10, 5), 15)
        self.assertEqual(math_func.add_func(-1, 1), 0)
        self.assertEqual(math_func.add_func(-1, -1), -2)

    def test_mult(self):
        self.assertEqual(math_func.mult_func(10, 5), 50)
        self.assertEqual(math_func.mult_func(-1, 1), -1)
        self.assertEqual(math_func.mult_func(-1, -1), 1)

    def test_div(self):
        self.assertEqual(math_func.div_func(10, 5), 2)
        self.assertEqual(math_func.div_func(-1, 1), -1)
        self.assertEqual(math_func.div_func(-1, -1), 1)
        self.assertEqual(math_func.div_func(5, 2), 2.5)
        with self.assertRaises(ValueError):
            math_func.div_func(10, 0)


if __name__ == '__main__':
    unittest.main()