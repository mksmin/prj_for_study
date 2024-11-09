import unittest
from unittest import TestCase
from unit_testing.solver import Solver


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.s = Solver(2, 3)

    def test_add(self):
        # s = Solver(2, 3)
        result = self.s.add()

        self.assertEqual(5, result)
        self.assertIsInstance(result, int)

    def test_mul(self):
        # s = Solver(2, 3)
        result = self.s.mul()
        self.assertEqual(6, result)

    def test_mul_raises_typeerror(self):
        s = Solver('', 0)
        with self.assertRaises(TypeError) as exc_info:
            s.mul()

        self.assertEqual(str(exc_info.exception), s.EXC_TEXT_INVALID_TYPE)

        print('exc info ex', str(exc_info.exception))
        print('exc info ex', exc_info)


if __name__ == '__main__':
    unittest.main()
