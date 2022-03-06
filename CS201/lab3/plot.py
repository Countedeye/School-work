#!/usr/bin/env python3

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
        print("This program is designed to take user input passed in as arguments and plot a cartesian plane in the terminal.")
        print("This program will need the user to input a point for the plane.")
        print("-v, --version    Prints the version of the program.")
        print("-h, --help       Prints this help text.")
        exit(0)


# def cartesian_plane(rows,columns):
columns=17
rows=17

points=[]

for argument in args:       # this for loop takes the argument and changes it from a string to a tuple of integers.
    point=argument.split(",")
    for index in range(len(point)): #this checks the argument from index 0 and identifies a coordinate
        coord=int(point[index])
        point[index]=coord          #this turns the index of point back into an integer.
    points.append(tuple(point))     #this adds a tuple of the integers point to points


def cartesian_plane(rows,columns):
    for y in range(rows//2, -(rows//2) -1, -1):
        for x in range(-(columns//2) +1,columns//2,1):
            currentPoints =(x,y)
            if y == 0 or (y == 8 and (x != 0 or x!= columns+1)) or (y == -8 and (x != 0 or x != columns+1)):
                print("-", end=" ")
            elif x == 0 or x==7 or x==-7 :
                print("|", end=" ")
            elif currentPoints in points:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

version(args)
help(args)
cartesian_plane(rows,columns)
