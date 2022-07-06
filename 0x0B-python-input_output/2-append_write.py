#!/usr/bin/python3

"""
Writing append files module
"""


def append_write(filename="", text=""):
    """Writes and append a text to a file

    Args:
        filename (:obj:`str`): The file name.
        text (:obj:`str`): The text to write into the file.
    Returns:
        (`int`): The number of character writen
    """
    res = 0
    if filename and text:
        with open(filename, 'a', encoding='utf-8') as f:
            res = f.write(text)
    return res
