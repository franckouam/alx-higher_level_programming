#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._Node__data

    @data.setter
    def data(self, data):
        if data and not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self._Node__data = data

    @property
    def next_node(self):
        return self._Node__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be an integer")
        else:
            self._Node__next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        res = ""
        tmp = self.head
        while tmp.next_node != None:
            res += str(tmp.data)
            tmp = tmp.next_node
            if tmp.next_node != None:
                res += "\n"
        return res

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            while value > tmp.data and tmp.next_node != None:
                prev = tmp
                tmp = tmp.next_node
            new_node.next_node = tmp
            if tmp == self.head:
                self.head = new_node
            else:
                prev.next_node = new_node
        
