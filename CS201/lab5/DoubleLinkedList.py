#!/usr/bin/env3 python3
import sys

args=sys.argv[1:]

from DoubleLinkedNode import DoubleLinkedNode as Node

class DoubleLinkedList:
    def __init__(self):
        self._length = 0
        self.start = None
        self.end = None

    def __len__(self):
        return self._length

    def _get_node(self, index):
        print(Node[0])
        pass

    def get_value(self, index):
        self._get_node(index)
        # Hint: Call `self._get_node(index)`
        pass

    def insert(self, index, val):
        self._get_node(index)
        # Hint: Use `self._get_node(index)` to get the node right before the insertion
        pass

    def append(self, val):
        self.insert(len())
        # Hint: Call `self.insert()` using the `len()` as the index
        pass

    def prepend(self, val):
        self.insert(0)
        # Hint: Call `self.insert()` using `0` as the index
        pass

    def remove(self, val):
        # for x in range(self.end):
        #     if node.value == val:
        #         node.value.pop()
        # Hint: Iterate from the start checking if `node.value == val`.
            pass

    def pop(self, index):
        self._get_node(index)
        # Hint: Call `self._get_node()` using index, or `len()` as the index
        pass

    def print_forward(self):

        node= self.start
        while node!= None:
            print(node.value)
            node = node.next
        # Iterate forward through the Linked List printing the value of each node.
        #   You may print the items out however you like as long there is a clear
        #   distinction between each element.  Here is one example, one element
        #   per line, with header and footer lines:
        print("---- DoubleLinkedList - Forward ---")
        node = self.start
        while node != None:
            print(node.value)
            node = node.next
        print("-------------------------------------")

    def print_reverse(self):
        node = self.end
        while node!= None:
            print(node.value)
            node = node.prev
        # Iterate backward through the Linked List printing the value of each node.
        pass


if __name__ == "__main__":
    print(f"==={__file__}=====")
