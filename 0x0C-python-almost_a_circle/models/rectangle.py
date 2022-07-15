#!/usr/bin/python3
"""
The `rectangle` module
"""
from models.base import Base


class Rectangle(Base):
    """The ``Rectangle`` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs a ``Rectangle`` object.

        Args:
            width (`int`): The width of the `Rectangle` instance.
            height (`int`): The height of the `Rectangle` instance.
            x (`int`): The x coordinate of the `Rectangle` instance.
            y (`int`): The y coordinate of the `Rectangle` instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
