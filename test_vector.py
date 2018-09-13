from vector import Vector
import unittest


class TestVector(unittest.TestCase):
    v = Vector([1, 2, 3])
    v1 = Vector([1, 1, 1])
    v_add = Vector([2, 3, 4])
    v_sub = Vector([0, 1, 2])
    v_mul = 6

    def test__len__(self):
        self.assertEqual(
            len(self.v),
            3)

    def test__getitem__(self):
        self.assertEqual(
            self.v[2],
            3)

    def test__add__(self):
        self.assertEqual(
            self.v + self.v1,
            self.v_add)

    def test__sub__(self):
        self.assertEqual(
            self.v - self.v1,
            self.v_sub)

    def test__mul__(self):
        self.assertEqual(
            self.v * self.v1,
            self.v_mul)
