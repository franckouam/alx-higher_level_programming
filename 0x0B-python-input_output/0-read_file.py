#!/usr/bin/python3

"""
Reading files module.
"""


def read_file(filename=""):
    """Reads a file and prints it

    Args:
        filename (:obj:`str`): The file name.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
