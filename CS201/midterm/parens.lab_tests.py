#!/usr/bin/env python3

from parens import in_parens

all_passed = True

test = "Hi, I'm Robert (Bob)."
if in_parens(test) != "Bob":
    print("Test 1 failed.")
    all_passed = False

test = "3 + (4 - x) / 2"
if in_parens(test) != "4 - x":
    print("Test 2 failed.")
    all_passed = False

test = "Hi"
if in_parens(test) != None:
    print("Test 3 failed.")
    all_passed = False

test = "Empty ()."
if in_parens(test) != "":
    print("Test 4 failed.")
    all_passed = False

test = "Look ) at ( this"
if in_parens(test) != None:
    print("Test 5 failed.")
    all_passed = False

if all_passed:
    print("All tests PASSED!")
