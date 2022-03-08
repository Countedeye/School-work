#!/usr/bin/env python3

import sys
import parens

args=sys.argv[1:]

from datetime import date


VERSION = date.today()

def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program uses standard input to run a program.")
        print("This program will need the user to input search string.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)

def tty_mode():
    args = []
    user_data = None
    while user_data != "":
        args.append(user_data)
        user_data = input(" Please enter an argument to pass through the program... {blank to quit}:")
        if user_data != "":
            print(parens.in_parens(user_data))

def pipe_mode():
    args = []
    user_data = None
    for line in sys.stdin:
        args.append(line.strip())
        print(parens.in_parens(line))

if __name__ == "__main__":
    # Argument processing
    if sys.stdin.isatty():
        tty_mode()
    else:
        pipe_mode()
