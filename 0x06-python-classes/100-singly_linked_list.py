#!/usr/bin/python3
"""create and manipulate a single link list"""


class Node:
    """creation of class node"""
    def __init__(self, data, next_node=None):
        """initialization of a node
            Args: data - value of node
            next_node - next node
            """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieving data node"""
        return self.__data

    @data.setter
    def data(self, value):
        """set a value for a node
            Args: value - value of a node"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """retrieving next_node of a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set a next node
        Args: value - value of the node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """creation of a class signle list"""
    def __init__(self):
        """initialize a link list"""
        self.head = None

    def __str__(self):
        """print a single link list"""
        printsll = ""
        tmp = self.head
        while tmp:
            printsll = printsll + str(tmp.data) + "\n"
            tmp = tmp.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert a node in a list
            Args: value - value of a node"""
        nod = Node(value)
        if not self.head:
            self.head = nod
            return
        if value < self.head.data:
            nod.next_node = self.head
            self.head = nod
            return
        else:
            tmp = self.head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node
            if tmp.next_node:
                nod.next_node = tmp.next_node
            tmp.next_node = nod
