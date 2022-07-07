#!/usr/bin/python3

"""
MyList module
"""


class MyList(list):
    """A class that inherits from `list`"""
    def __init__(self, *args, **kwargs):
        """Construct ``MyList`` instances."""
        super(list).__init__(*args, **kwargs)

    def print_sorted(self):
        """Prints the sorted list(ascending sort)"""
        super(list).sort()
        print(self)
