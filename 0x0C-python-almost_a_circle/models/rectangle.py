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
