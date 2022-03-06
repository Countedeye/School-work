#!/usr/bin/env python3

import sys
import datetime

args = sys.argv[1:]

from datetime import date       #imports updated date


canRead = "-r" in sys.argv or "--read" in sys.argv
canWrite = "-w" in sys.argv or "--write" in sys.argv
canExecute = "-x" in sys.argv or "--execute" in sys.argv
version = date.today()          #changes date to current date

if canRead and canWrite and canExecute:
    print(7)
elif canRead and canWrite and not canExecute:
    print(6)
elif canExecute and canRead and not canWrite:
    print(5)
elif canWrite and canExecute and not canRead:
    print(3)
elif canRead and not canWrite and not canExecute:
    print(4)
elif canWrite and not canRead and not canExecute:
    print(2)
elif canExecute and not canRead and not canWrite:
    print(1)
elif "-h" in args or "--help" in args:
    print("This program should print out all arguments provided in the command line. These arguments will be one per line.")
    print("Options:")
    print("-r, --read       Prints out the read executable.")
    print("-w, --write      Prints out the write executable.")
    print("-e, --excute     Prints out the execute executable.")
    print("-v, --version    Prints the version of the program.")
    print("-h, --help       Prints this help text.")
    exit(0)
elif "-v" in args or  "--version" in args:
    print(version)
    exit(0)
else:
    print(0)
