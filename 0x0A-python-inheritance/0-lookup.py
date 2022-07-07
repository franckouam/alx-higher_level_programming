"""The lookup module
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj (`Any`): The object on whose attributes should be returned.
    Returns:
        (:obj: `list`): The list of attributes.
    """
    return dir(obj)
