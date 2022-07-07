
"""
Student definition module
"""


class Student:
    """A student definition class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a ``Student``.

        Args:
            attrs (:obj:`list` of `str`, optional): The list of attributes
                                                    to retrieve.
        Returns:
            (`dict`)
        """
        d = {}
        if attrs:
            for a in attrs:
                try:
                    d[a] = self.__getattribute__(a)
                except Exception:
                    pass
        else:
            d['first_name'] = self.first_name
            d['last_name'] = self.last_name
            d['age'] = self.age
        return d

    def reload_from_json(self, json):
        """Replaces all attributes of the ``Student`` instance.

        Args:
            json (`dict`): The dictionnary of attributes to replace.
        """
        for key, value in json.items():
            setattr(self, key, value)
