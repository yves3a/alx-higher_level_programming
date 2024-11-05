#!/usr/bin/python3
"""
Module
Defines a class that defines a singly linked list node
"""


class Node:
    """creating a class that defines a node"""

    def __init__(self, data, next_node=None):
        """Initailises a class """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retreiving a private instance data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setting an instance data

        Args
            Data: must be int,
            Value: value to be assigned
        Raises:
        TypeError, if data is not int
        """
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """Retreiving the pointer"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting the pointer"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.

    Attributes:
        __head: Private instance attribute representing the head of the list
    """
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value: The value to insert into the list
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        String representation of the linked list.

        Returns:
            str: String representation of the list with one node number a line
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
