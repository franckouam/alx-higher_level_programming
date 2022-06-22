#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def __eq__(self, other):
        return self.area() == other.area()

    def __nq__(self, other):
        return self.area() != other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.size < other.size

    def area(self):
        return self._Square__size ** 2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
