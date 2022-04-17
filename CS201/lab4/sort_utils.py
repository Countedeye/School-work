#!/usr/bin/env python3

import sys

args= sys.argv[1:]


VERSION="0.0.1"

verbose = True

def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program is designed to sort through a list.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)

swaps = []
def swap_tracker_reset():
    global swaps
    swaps = []


def swap(li, i, j):

    # Track swaps
    low = min(i, j)
    hi = max(i, j)
    swaps.append(((low, li[low]),(hi, li[hi])))
    count=0
    var1= ""
    var2= ""
    for index in li:
        if count == i:
            var1 = index
        elif count == j:
            var2 = index
        count +=1
    li[i]= var2
    li[j]= var1

    return li


    if verbose:
        print(li)
        print(f"swap {low}:{li[low]} <--> {hi}:{li[hi]}")

    # You add the code to actually swap list values here

    return

if __name__ == "__main__":
    print(f'Running tests for "{__file__}"...')

    # You add your own tests here.
# print(swap(list("defabi"),2,3))
# print(swap(list("bacdef"),0,1))
