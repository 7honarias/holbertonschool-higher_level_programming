#!/usr/bin/python3
"""Defines a singly linked list"""


class Node():
    """Class that defines a node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is not True:
                raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter of next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter of next_node.
        """
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList():
    """Class that defines a singly linked list"""

    def __init__(self):
        """Method for initialize a single list
        """
        self.__head = None

    def sorted_insert(self, value):
        """Method to manage a insert new node
        """
        new_node = Node(value, None)
        tmp = self.__head
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Method to print Square instance.
        """

        if self.__head is None:
            return ""
        temp = self.__head
        lista = ""
        while temp:
            lista += str(temp.data) + "\n"
            temp = temp.next_node

        return lista[:-1]
