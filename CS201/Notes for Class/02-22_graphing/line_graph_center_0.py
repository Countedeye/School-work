#!/usr/bin/env python3


bg_str = "--------|--------"
# bg = ["|", "-", "-"]

def new_graph():
    return list(bg_str)

def print_graph(g):
    print("        0")
    print("".join(g))

def plot_point(g, x, ch="X"):
    g[x + 8] = ch


g1 = new_graph()
plot_point(g1, 2)
plot_point(g1, -3, "*")
print_graph(g1)
