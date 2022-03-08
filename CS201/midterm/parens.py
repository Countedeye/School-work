#!/usr/bin/env python3

import os
import sys
import datetime

args=sys.argv[1: ]

from datetime import date


VERSION = date.today()

def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program is designed to take user input passed in as arguments to search for and return any text inside of the first set of parentheses.")
        print("This program will need the user to input search string.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)

def in_parens(args):
    if "(" in args:
        pos1 = args.find("(")
        if ")" in args:
            pos2 = args.find(")")
            if pos2 < pos1:
                return None
            replaced = args.replace("(", "").replace(")","")
            slicedPosition= replaced[slice(pos1, pos2 -1)]
            return slicedPosition
        else:
            return None
    else:
        return None

version(args)
help(args)
in_parens(args)

#if __name__ == "__main__":
#    print(f"Running test for module {__file__}...")
