from typing import List, Union
from vector import Vector


class Matrix(Vector):
    def __init__(self, matrix: List[Union[Vector, List]]):
        if any([len(matrix[0]) != len(matrix[i]) for i in range(len(matrix))]):
            raise Exception("Columns should have same length")
        self.matrix = [Vector(i) for i in matrix]

    def __iter__(self):
        for row in self.matrix:
            yield row

    def __getitem__(self, key):
        return self.matrix[key]

    def __len__(self):
        return len(self.matrix)

    def row(self, key: int) -> Vector:
        if key < self.shape[0]:
            return self.matrix[key]
        else:
            e = "Wrong key, here only {} rows".format(self.shape[0])
            raise Exception(e)

    def col(self, key: int) -> Vector:
        if key < self.shape[1]:
            return Vector([row[key] for row in self.matrix])
        else:
            e = "Wrong key, here only {} cols".format(self.shape[1])
            raise Exception(e)

    @property
    def shape(self):
        return (len(self), len(self[0]))

    def __eq__(self, other):
        return self[0] == other[0]
        return all([self[i] == other[i] for i in range(len(self))])
