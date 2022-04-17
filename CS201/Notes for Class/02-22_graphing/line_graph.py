#!/usr/bin/env python3


bg_str = "|------------------------|"
# bg = ["|", "-", "-"]

def new_graph():
    return list(bg_str)

def print_graph(g):
    print("0")
    print("".join(g))

g1 = new_graph()
print_graph(g1)

g1[7] = "X"
print_graph(g1)
