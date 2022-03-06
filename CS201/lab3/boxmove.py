#!/usr/bin/env python3

import sys
import datetime

args = sys.argv[1: ]

from datetime import date

VERSION = date.today()


def version(args):
    if "-v" in args or  "--version" in args:
        print(VERSION)
        exit(0)

def help(args):
    if "-h" in args or "--help" in args:
        print("This program is designed to take user input and move the astrick within the bounds of the box.")
        print("This program will need the user to input a direction and count integer.")
        print("This will move the location of the astrick.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)


rows=13
columns=23


pos_row = rows // 2
pos_column = columns // 2

def box():
    for row in range(rows):
        for column in range(columns):
            if row == pos_row and column == pos_column:
                print("*",end="")
            elif row == 0 or row == rows -1:
                print("-", end="")
            elif column == 0 or column == columns -1:
                print("|", end="")
            else:
                print(" ",end="")          # end =" " stops a newline from forming
        print()                         # inner for loop new line
box()

def move(direction, count):
    global pos_row
    global pos_column
    r = pos_row
    c = pos_column
    if direction == "U":
        r -= count
    elif direction == "D":
        r += count
    elif direction == "L":
        c -= count
    elif direction == "R":
        c += count

    if c < 0 or r < 0 or c >= columns or r >= rows:
        print("this move is beyond the bounds of the box.")
    else:
        pos_row = r
        pos_column = c

#Main Function
while True:
    box()
    userdata =  input("Enter a direction and a positive number (e.g. U5, L4, R2, D1): ")
    if userdata == "":
        print("Empty input detected.")
        break
        direction = userdata[0].upper()
        count = int(userdata[1:])
        move(direction,count)

print("Program complete.")


version(args)
help(args)
