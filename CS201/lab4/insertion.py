#!/usr/bin/env python3
import sys
import sort_utils

args=sys.argv[1:]
VERSION="0.0.1"

def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program is designed to use insertion sort through a list.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)
def insertion_sort(li):
    sort_utils.swap_tracker_reset()
    for i in range(len(li)-1):
        for j in range(i+1,0,-1):
            value_before= j-1
            if li[j] < li[value_before]:
                sort_utils.swap(li, j, value_before)
            else:
                break
    return li


# if __name__ == "__main__":
    # print(insertion_sort(list("90432567")))
