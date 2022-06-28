#!/usr/bin/python3
"""A simple module to define a ``Rectangle``
"""


class Rectangle:
    """A simple ``Rectangle`` class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructs a ``Rectangle`` object

        Args:
            width (`int`): The ``width`` of the ``Rectangle``
                 height (`int`): The ``height`` of the ``Rectangle``
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Args:
            height (`int`): The height of the ``Rectangle``
        Raises:
            TypeError: if ``height`` is not an integer
            ValueError: if ``height`` < 0
        """
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = height

    @property
    def width(self):
        """
        Args:
            width (`int`): The width of the ``Rectangle``
        Raises:
            TypeError: if ``width`` is not an integer
            ValueError: if ``width`` < 0
        """
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = width

    def area(self):
        """Computes the ``area`` of the ``Rectangle``"""
        return self.width * self.height

    def perimeter(self):
        """Computes the ``perimeter`` of the ``Rectangle``"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        res = ""
        for i in range(self.height):
            for __ in range(self.width):
                res += str(self.print_symbol)
            if i < self.height - 1:
                res += "\n"
        return res

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Compares two ``Rectangles`` and returns the biggest

        Args:
            rect_1 (:class: `Rectangle`): The first ``Rectangle``
            rect_2 (:class: `Rectangle`): The second ``Rectangle``
        Returns:
           (:class: `Rectangle`)
        Raises:
            TypeError: if ``rect_1`` or ``rect_2`` is not a ``Rectangle``.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square"""
        return cls(size, size)
