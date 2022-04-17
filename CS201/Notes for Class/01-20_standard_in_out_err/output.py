#!/usr/bin/env python3

import sys

user_data = input("Type something: ")
x = 23

print(f"Standard Output {user_data} {x}")
print(f"Standard Error {user_data} {x}", file=sys.stderr)
