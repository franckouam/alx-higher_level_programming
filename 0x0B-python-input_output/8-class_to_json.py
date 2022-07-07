
"""
Class to JSON module
"""


def class_to_json(obj):
    """Returns the dictionary decription of an object"""
    attribs = dir(obj)
    res = {}
    for a in attribs:
        if obj.__getattribute__(a):
            res[a] = obj.__getattribute__(a)
    return res
