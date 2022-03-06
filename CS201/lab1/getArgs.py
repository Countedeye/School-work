#!/usr/bin/env python3
import sys

args = sys.argv[1:]

version = "0.0.1"

if "-h" in args or "--help" in args:
    print("This program should print out all arguments provided in the command line. These arguments will be one per line.")
    print("Options:")
    print("-v, --version    Prints the version of the program.")
    print("-h, --help       Prints this help text.")
    exit(0)


if "-v" in args or  "--version" in args:
    print(version)
    exit(0)


if len(args) == 0:
    print("You must provide arguments to this program.", file=sys.stderr)
    exit(1)

for arg in args:
    print(arg)
