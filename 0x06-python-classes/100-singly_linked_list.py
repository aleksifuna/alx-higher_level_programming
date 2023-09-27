#!/usr/bin/python3
"""
contains defination of class Node and class SinglyLinkedList
to manupilate the nodes
"""


class Node:
    """
    belongs to a singly linked list with private instance data and next node
    """
    def __init__(self, data, next_node=None):
        """
        initializes the class node.

        Args:
            data: integer value stored in the node
            next_node: next node on the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data from node.
        Returns:
            data from the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """validates the value of data
        Args:
            value: data for the node
        Raises:
            TypeError: if data is not integer

        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next_node from node.
        Returns:
            next node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """validates the value of next_node
        Args:
            value: next_node
        Raises:
            TypeError: if data is not node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """links the nodes and has private instances head and
    methods to insert and retrieve data
    """
    def __init__(self):
        """Initializes the class SinglyLinkedList
        """
        self._head = None

    def sorted_insert(self, value):
        """inserts a new node into the correct sorted position in the list
        Args:
            value: the value to be inserted into the linked list
        """
        newnode = Node(value)
        if not self._head or value < self._head.data:
            newnode.next_node = self._head
            self._head = newnode
            return
        current = self._head
        while current.next_node and value > current.next_node.data:
            current = current.next_node
        newnode.next_node = current.next_node
        current.next_node = newnode

    def __repr__(self):
        """returns the content of the linked list.
        Returns:
            content of linked list.
        """
        string = ""
        current = self._head
        while current:
            string += str(current.data)
            if current.next_node:
                string += "\n"
            current = current.next_node
        return string
