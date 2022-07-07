#!/usr/bin/python3

"""
Writting in file module
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a text to a file, after each line containing a special string"""
    doc = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            doc.append(line)
            if line.find(search_string) != -1:
                doc.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        for line in doc:
            f.write(line)
