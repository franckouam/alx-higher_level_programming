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
        self._validate_or_raise(width, 'width')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self._validate_or_raise(height, 'height')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self._validate_or_raise(x, 'x')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self._validate_or_raise(y, 'y')
        self.__y = y

    def _validate_or_raise(self, attr, name):
        if type(attr) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ['width', 'height']:
            if attr <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name in ['x', 'y']:
            if attr < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Compute the `Rectangle` area"""
        return self.width * self.height

    def display(self):
        res = ""
        for i in range(self.height):
            for __ in range(self.width):
                res += '#'
            if i < self.height - 1:
                res += "\n"
        print(res)

    def __str__(self):
        res = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        res += f"- {self.width}/{self.height}"
        return res
