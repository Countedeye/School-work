#!/usr/bin/env python3

import sys
import datetime

args = sys.argv[1:]

from datetime import date

VERSION = date.today()

di = {}

if "-v" in args or  "--version" in args:
    print(VERSION)
    exit(0)
elif "-h" in args or "--help" in args:
    print("This program creates a dictionary of labeled pairs of arguments.")
    print("This program should not pout hyphens on the names of arguments." )
else:
    pass

for arg in args:
    key_value_list= (arg.split("="))
    key_value_list[0] = key_value_list[0].strip("-")

    try:
        key_value_list[1] = int(key_value_list[1])
    except ValueError:
        try:                    #requires an except statement
            key_value_list[1] = float(key_value_list[1])
        except ValueError:
            pass                #allows an empty code block


    di[pair[0]] = pair[1]
    print(key_value_list)


print(di)
