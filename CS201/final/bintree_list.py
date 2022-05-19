#!/usr/bin/env python3

from bintree_print import print_list_tree
treedata = []
for i in range(0, 15):
    treedata.append(i)
print(treedata)
print_list_tree(treedata)


def get_left_index(index):
    return 2*index +1

def get_right_index(index):
    return 2*index +2

print("===== Breadth First Traversal:")
for i in range(len(treedata)):
    print(f"{treedata[i]} ", end="")
print()


print("===== Depth First Traversal")

def dft(index, type):
    print(f"-- {type} traversal:")
    _dft(0, type)
    print()


def _dft(index, type):

    #preorder
    if type == "preorder":
        print(f"{treedata[index]} ", end="")

    l_index = get_left_index(index)
    if l_index < len(treedata):
        _dft(l_index, type)

    if type == "inorder":
        print(f"{treedata[index]} ", end="")

    r_index = get_right_index(index)
    if r_index < len(treedata):
        _dft(r_index, type)


    if type == "postorder":
        print(f"{treedata[index]} ", end="")


dft(0, "preorder")
dft(0, "inorder")
dft(0, "postorder")
