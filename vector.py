from typing import List


class Vector:
    def __init__(self, vector: List[int]):
        if not all([isinstance(i, int) for i in vector]):
            raise Exception('Vector must be a list with ints')
        self._vector = vector
        self.vector = self._vector[:]

    def __str__(self) -> str:
        return ' ' + ' '.join([str(v) for v in self]) + '\n'

    def __len__(self) -> int:
        return len(self.vector)

    def __getitem__(self, key: int):
        return self.vector[key]

    def __iter__(self):
        for i in self.vector:
            yield i

    def __add__(self, other):
        if len(self) != len(other):
            raise Exception("Vectors dimension doesn't match")
        return Vector([self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        if len(self) != len(other):
            raise Exception("Vectors dimension doesn't match")
        return Vector([self[i] - other[i] for i in range(len(self))])

    def __mul__(self, other):
        if len(self) != len(other):
            raise Exception("Vectors dimension doesn't match")
        return sum([self[i] * other[i] for i in range(len(self))])

    def __eq__(self, other):
        return self.vector == other.vector


v1 = Vector([1, 2, 3])
# print(v1)
