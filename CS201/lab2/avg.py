#!/usr/bin/env python3

import sys
import datetime

args = sys.argv[1:]

from datetime import date

VERSION = date.today()

numbers = []

user_answer = input("enter a minimum and maximum argument.")

if "-v" in args or  "--version" in args:
    print(VERSION)
    exit(0)
elif "-h" in args or "--help" in args:
    print("This program will operate in 3 different modes.")
    print("")

else:
    pass


def arguments(args, numbers):               #function for arguments
    for argument in args:
        try:
            numbers.append(float())
        except:
            print("Couldnt convert \"{a}\" to a float.")


def tty_arguments(args, numbers):           #function for tty
    while user_answer != "":
        try:
            numbers.append(float(user_answer))
        except:
            print("Not correct data. Couldn't convert \"{user_answer}\" to a float.")


def pipe_input(args, numbers):              #function for pipe
    for line in sys.stdin:
        s= line.strip()
        try:
            numbers.append(float(s))
        except:
            pass


arguments(args, numbers)
tty_arguments(args, numbers)
pipe_input(args, numbers)
