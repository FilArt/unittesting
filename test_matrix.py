import unittest
from matrix import Matrix
from vector import Vector


class TestMatrix(unittest.TestCase):
    m1 = Matrix([[1, 2, 3]])
    m2 = Matrix([Vector([1, 2, 3])])
    m3 = Matrix([[1, 2, 3], [4, 5, 6]])

    def test__init__(self):
        self.assertEqual(self.m1, self.m2)

    def test__getitem__(self):
        self.assertEqual(
            self.m1[0],
            Vector([1, 2, 3]))

    def test__len__(self):
        self.assertEqual(
            len(self.m1),
            1)

    def test_shape(self):
        self.assertEqual(
            self.m3.shape,
            (2, 3))

    def test_row(self):
        self.assertEqual(
            self.m1.row(0),
            Vector([1, 2, 3]))

    def test_col(self):
        self.assertEqual(
            self.m1.col(0),
            Vector([1]))
