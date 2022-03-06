#!/usr/bin/env python3

import sys
import datetime

args = sys.argv[1: ]

from datetime import date

VERSION = date.today()


if len(args) < 2:           #if arguments are less than 2 this defaults arguments to 8.
    rows = 8
    columns = 8
else:
    rows = int(args[0])         #rows would be first argument
    columns = int(args[1])      #columns are second argument


def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program is designed to take user input passed in as arguments and create a box.")
        print("This program will need the user to input a row and column integer.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)

def box(rows,columns):
    for y in range(rows):
        for x in range(columns):
            if (x == 0 and (y == 0 or y== rows-1)) or (x == columns-1 and (y == 0 or y==rows-1)):
                print('+',end=" ")
            elif (y != 0 and (x == 0 or x== columns-1)) or (y != rows-1 and (x == 0 or x ==columns-1)):
                print('|', end=" ")
            elif (y == 0 and (x != 0 or x!= columns-1)) or (y == rows-1 and (x != 0 or x != columns-1)):
                print('-',end=" ")
            else:
                print(" ",end=" ")          # end =" " stops a newline from forming
        print("\n")                         # inner for loop new line

version(args)
help(args)
box(rows,columns)
