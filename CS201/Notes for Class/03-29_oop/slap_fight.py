#!/usr/bin/env python3

import random
import time

from Character import Character

with open("names.txt", "r") as f:
    names = f.read().strip().split("\n")


colors = [
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
]

chars = []
num_chars = 6

for i in range(num_chars):
    name = random.choice(names)

    color = random.choice(colors)
    bkg_col = random.choice(colors)

    while color == bkg_col:
        bkg_col = random.choice(colors)

    c = Character(name, color, bkg_col)
    chars.append(c)



for c in chars:
    print(c)

def one_is_dead():
    for c in chars:
        if c.health <= 0:
            return c
    return False


print("----- Fight -----")

while not one_is_dead():
    c1 = random.choice(chars)
    c2 = random.choice(chars)
    c1.slap(c2)
    if random.uniform(0, 1) < 0.25:
        print("COUNTER!")
        c2.slap(c1)
    time.sleep(1)
