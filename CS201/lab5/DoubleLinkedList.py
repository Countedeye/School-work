#!/usr/bin/env3 python3

from DoubleLinkedNode import DoubleLinkedNode as Node

class DoubleLinkedList:


    def __init__(self):
        self._length = 0
        self.start = None
        self.end = None


    def __len__(self):
        return self._length


    def _get_node(self, index):
        if index < 0 or index >= self._length:
                raise IndexError
        if index < self._length / 2 :
            current_node = self.start
            current_index = 0
            while current_index < index:
                current_node = current_node.next
                current_index += 1

            return current_node
        else:
            current_node = self.end
            current_index = self._length - 1

            while current_index > index:
                current_node = current_node.prev
                current_index -= 1
        return current_node
        pass


    def get_value(self, index):
        return self._get_node(index).value
        # # Hint: Call `self._get_node(index)`
        pass


    def insert(self, index, val):
        if index > self._length or index < 0:
            raise IndexError

        new_node = Node(val)

        if self._length == 0:
            self.start= new_node
            self.end= new_node
            self._length +=1
            return

        if index == 0:
            first_node = self.start
            self.start = new_node
            new_node.next = first_node
            first_node.prev = new_node
            self._length +=1
            return

        if index == self._length:
            last_node = self.end
            self.end = new_node
            new_node.prev = last_node
            last_node.next = new_node
            self._length += 1
            return

        return self._get_node(index)
        pass


    def append(self, val):
        index = self._length
        self.insert(index, val)
        pass


    def prepend(self, val):
        return self.insert(0, val)
        # Hint: Call `self.insert()` using `0` as the index
        pass


    def remove(self, val):

        if self._length == 0:
            return ValueError

        current_node = self.start
        current_index = 0

        while current_node.value != val and current_index < self._length:
            current_node = current_node.next
            current_index += 1

        if current_index == self._length:
            return

        return self.pop(current_index)
        pass


    def pop(self, index):
        if index >= self._length or index < 0:
            raise IndexError

        if index == 0: #removes first
            first_node = self.start
            self.start = first_node.next
            del first_node
            self._length -= 1
            return

        if index == self._length -1: #removes last
            last_node = self.end
            self.end = last_node.prev
            del last_node
            self._length -= 1
            return

        remove_node = self._get_node(index)
        before_node = remove_node.prev
        after_node = remove_node.next

        before_node.next = after_node
        after_node.prev = before_node

        self._length -= 1
        del remove_node
        return
        pass


    def print_forward(self):
        print("---- DoubleLinkedList - Forward ---")
        if self._length != 0:
            current_node = self.start
            current_index = 0
            while current_index < self._length:
                print(current_node.value)
                current_node = current_node.next
                current_index += 1
        pass
        print("-------------------------------------")


    def print_reverse(self):
        print("---- DoubleLinkedList - Reverse ---")
        if self._length != 0:
            current_node = self.end
            current_index = self._length -1
            while current_index >= 0:
                print(current_node.value)
                current_index -= 1
                current_node -= current_node.prev
        print("-------------------------------------")
        # Iterate backward through the Linked List printing the value of each node.
        pass


# if __name__ == "__main__":
#
#     dll = DoubleLinkedList()
#
#     a= Node("Alligator")
#     b= Node("Bird")
#     c= Node("Cat")
#     d= Node("Dog")
#     e= Node("Elephant")
#
#
# a.next= b
# b.prev=a
#
# b.next=c
# c.prev=b
# dll.start = a
# dll.end = e
# dll._length = 5
#
# dll.insert(0, "foo")
# print(dll.get_value(0))
# print(dll.get_value(4))
# print(len(dll))
