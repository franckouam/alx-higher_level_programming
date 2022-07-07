#!/usr/bin/python3

"""
MyList module
"""


class MyList(list):
    """A class that inherits from `list`"""
    def __init__(self, *args, **kwargs):
        super(list).__init__(*args, **kwargs)

    def print_sorted(self):
        self.sort()
        print(self)
