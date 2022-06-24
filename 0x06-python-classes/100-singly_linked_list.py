#!/usr/bin/python3
"""A module of singly linked list using python.

This module implements a basic singly list
"""


class Node:
    """The ``Node`` of singly linked list
    """
    def __init__(self, data, next_node=None):
        """Constructs ``Node`` object.

        Args:
            data (`int`): The data of the ``Node``.
            next_node (:obj:`Node`, optional): The next ``Node``.

        Raises:
            TypeError: If ``data`` is not an integer.
                If ``next_node`` is not a ``Node`` objet.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Args:
            data (`int`): The data of the ``Node``.

        Raises:
            TypeError: If ``data`` is not an integer.
        """
        return self._Node__data

    @data.setter
    def data(self, data):
        if data and not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self._Node__data = data

    @property
    def next_node(self):
        """
        Args:
            data (`int`): The data of the ``Node``.

        Raises:
            TypeError: If ``data`` is not an integer.
        """

        return self._Node__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be an integer")
        else:
            self._Node__next_node = next_node


class SinglyLinkedList:
    """Definition of a ``singly linked list``.
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        res = ""
        tmp = self.head
        while tmp.next_node is not None:
            res += str(tmp.data)
            tmp = tmp.next_node
            if tmp.next_node is not None:
                res += "\n"
        return res

    def sorted_insert(self, value):
        """Inserts in a sorted ``singly linked list``

        Args:
            value (`int`): The value to insert.
        """
        try:
            new_node = Node(value)
        except Exception:
            return
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            while value > tmp.data and tmp.next_node is not None:
                prev = tmp
                tmp = tmp.next_node
            new_node.next_node = tmp
            if tmp == self.head:
                self.head = new_node
            else:
                prev.next_node = new_node
