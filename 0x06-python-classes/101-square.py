#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        res = ""
        if self.size:
            line = " " * self.position[0] + "#" * self.size
            res = "\n" * self.position[1]
            res += (line + "\n") * (self.size - 1)
            res += line
        return res

    def area(self):
        return self.size ** 2

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

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = position

    def my_print(self):
        print(self)
