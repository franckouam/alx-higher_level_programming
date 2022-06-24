#!/usr/bin/python3
"""Square module definition.

This module defines a simple `Square` class
"""


class Square:
    """A simple ``Square`` class

    Attributes:
        size (`int`): The size of the ``Square``.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructs a ``Square`` objet
        Args:
            size (`int`): The size of the ``Square``.
                The default value is 0.

        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` < 0
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of the ``Square``.
        Returns:
            int: The area of the ``Square``.
        """
        return self.size ** 2

    @property
    def size(self):
        """
        Args:
            size (`int`): The size of the ``Square``.
                The default value is 0.

        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` < 0
        """
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
        """
        Args:
            position (:obj: `tuple` of `int`): The position to start to
                print the ``Square``.

        Raises:
            TypeError: If ``position`` is not a tuple of 2 integers
        """
        return self._Square__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = position

    def my_print(self):
        """Prints a ``Square`` filled with '#'"""
        if self.size:
            for i in range(self.size):
                print(" " * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
