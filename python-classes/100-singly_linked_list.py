#!/usr/bin/python3
"""Module that defines a class Node"""


class Node:
    """Class that defines a node"""
    def __init__(self, data, next_node=None):
        """Initialisation on variable atributes"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data atribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""
    def __init__(self):
        """Initialisation of the singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a node in a sorted way"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None:
            if current.next_node.data > value:
                break
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """String representation of the singly linked list"""
        current = self.head
        string = ""
        while current is not None:
            string += str(current.data)
            if current.next_node is not None:
                string += "\n"
            current = current.next_node
        return string
