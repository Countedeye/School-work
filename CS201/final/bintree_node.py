#!/usr/bin/env python3

from bintree_print import print_node_tree

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length


    def get(self, index):
        if self.length == 0 or index >= self.length or index < 0:
            return
        visit_queue = [self.root]
        i = 0
        while i != index:
            node = visit_queue.pop(0)
            if node.left:
                visit_queue.append(node.left)
            if node.right:
                visit_queue.append(node.right)
            i+= 1
        return visit_queue.pop(0).value

    def add(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            self.length += 1
            return
        visit_queue = [self.root]
        while len(visit_queue):
            node = visit_queue.pop(0)
            if node.left:
                visit_queue.append(node.left)
            else:
                node.left = new_node
                self.length += 1
                return
            if node.right:
                visit_queue.append(node.right)
            else:
                node.right = new_node
                self.length += 1
                return

if __name__ == "__main__":

    print(f"Running test for {__file__}...")


    # root = Node(0)
    # n1 = Node(1)
    # n2 = Node(2)
    # n3 = Node(3)
    #
    # root.left = n1
    # root. right = n2
    # root.left.left = n3
    #
    # print(root.value)
    # print(root.left.value)
    # print(root.right.value)
    # print(root.left.left.value)


    tree = Tree()

    for i in range(15):
        tree.add(i)

    print_node_tree(tree)

    def get_left_index(index):
        return 2*index +1

    def get_right_index(index):
        return 2*index +2

    print("===== Breadth First Traversal:")
    for i in range(len(tree)):
        print(f"{tree.get(i)} ", end="")
    print()


    print("===== Depth First Traversal")


    def dft(index, type):
        print(f"-- {type} traversal:")
        _dft(0, type)
        print()


    def _dft(index, type):

        #preorder
        if type == "preorder":
            print(f"{tree.get(index)} ", end="")

        l_index = get_left_index(index)
        if l_index < len(tree):
            _dft(l_index, type)

        if type == "inorder":
            print(f"{tree.get(index)} ", end="")

        r_index = get_right_index(index)
        if r_index < len(tree):
            _dft(r_index, type)


        if type == "postorder":
            print(f"{tree.get(index)} ", end="")


dft(0, "preorder")
dft(0, "inorder")
dft(0, "postorder")


    # print(tree.root.left.left.value)
    # print("length", len(tree))
