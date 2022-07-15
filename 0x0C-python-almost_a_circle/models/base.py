#!/usr/bin/python3
"""
Base module
"""


class Base:
    """The base class of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructs a ``Base`` object

        Args:
            id (`int`): The identifier of the object.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
