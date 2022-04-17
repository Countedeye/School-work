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
        print("This program is designed to use selection sort through a list.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)


def selection_sort(li):
    sort_utils.swap_tracker_reset()
    for i in range(len(li)- 1):
        index_smallest = i
        for j in range(i+1, len(li)):
            if li[j] < li[index_smallest]:
                index_smallest = j
        if index_smallest != 0:
            sort_utils.swap(li, index_smallest,i)
    return li




# if __name__ == "__main__":
    # print(selection_sort(list("8573219")))
