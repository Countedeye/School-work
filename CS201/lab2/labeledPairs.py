#!/usr/bin/env python3

import sys
import json

args = sys.argv[1:]

def jprint(item):
    print(json.dumps(item, indent =4))

VERSION = "0.0.1"

dictionary = {}

if "-v" in args or "--version" in args:
    print(VERSION)
    exit(0)

if "-h" in args or "--help" in args:
    print("A program to place labeled paris of arguments into a dictionary.")
    print("Arguments are expected in the form label, value, label, value, etc.")
    print("Example:")
    print(" ./labeledPairs.py --fruit grapes --veggie cucumber -c 47")
    exit(0)

if len(args) == 0:
    msg = "Must contain arguments of the form label, value, label, value, etc."
    print(msg, file=sys.stderr)
    exit(1)

while len(args):         # will stop when len(args) ==0
    label = args.pop(0)
    value = args.pop(0)

    label = label.strip("-") #removes excess hyphens
    try:
        value = int(value)
    except ValueError:
        try:
            value = value
        except float(ValueError):
            pass

dictionary[label] = value

jprint(dictionary)
