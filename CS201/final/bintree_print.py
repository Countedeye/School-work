#!/usr/bin/env python3

import math


# Print List-based Binary Tree
def _plt_recursion(list_tree, level=0, index=0, width=80):
    num_on_level = 2**level
    term_i = 0
    print(level, end="")
    for i in range(num_on_level):
        val = list_tree[index]
        pos = (i+1) * (width / (num_on_level + 1))
        glyph = "("+str(val)+")"
        multiplier = math.floor(pos - term_i - len(glyph)/2)
        term_i += multiplier + len(glyph)
        padding = " " * multiplier
        print(padding + glyph, end="")
        index += 1
        if index >= len(list_tree):
            break
    print()
    print("-"*width)
    if index < len(list_tree):
        _plt_recursion(list_tree, level+1, index, width)

def print_list_tree(list_tree, width=80):
    print("="*width)
    _plt_recursion(list_tree, 0, 0, width)


# Print Node-based Binary Tree
def _pnt_recursion(node_tree, level=0, index=0, width=80):
    num_on_level = 2**level
    term_i = 0
    print(level, end="")
    for i in range(num_on_level):
        val = node_tree.get(index)
        pos = (i+1) * (width / (num_on_level + 1))
        glyph = "("+str(val)+")"
        multiplier = math.floor(pos - term_i - len(glyph)/2)
        term_i += multiplier + len(glyph)
        padding = " " * multiplier
        print(padding + glyph, end="")
        index += 1
        if index >= len(node_tree):
            break
    print()
    print("-"*width)
    if index < len(node_tree):
        _pnt_recursion(node_tree, level+1, index, width)

def print_node_tree(node_tree, width=80):
    print("="*width)
    _pnt_recursion(node_tree, 0, 0, width)
