#!/usr/bin/env python3

import random
import sys

from datetime import date

args = sys.argv[1:]

VERSION = date.today()


min= 0.0
max = 100.0

if "-v" in args or  "--version" in args:
    print(VERSION)
    exit(0)
elif "-h" in args or "--help" in args:
    print("This program will generate a list of random floating point decimals.")
    print("This program should accept an optional named argument for maximan value and minimum value.")
    print("-M or --max defaulting to 100.0")
    print("-m or --min defaulting to 0.00")
else:
    pass


def min(args, min):
    if user_answer < 0.0:
        try:
            min.append(float(user_answer))
        except:
            print("Could not convert user input..")

def max(args, max):
    if user_answer < 100.0:
        try:
            max.append(float(user_anser))
        except:
            print("could not conver user input..")

r = random.uniform(min,max)


min(args,min)
max(args,max)

print(r)
