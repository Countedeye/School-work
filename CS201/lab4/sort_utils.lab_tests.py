#!/usr/bin/env python3

import sort_utils

tests_passed = 0
total_tests = 0

test_name = "Test 1"
print(f"---- {test_name} ----------------------------")
orig = list("abcdef")
li = list(orig)
sort_utils.swap(li, 2, 3)
print(li)
print("----------------------------------------")

total_tests+= 1
expected = list("abdcef")
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")


test_name = "Test 2"
print(f"---- {test_name} ----------------------------")
orig = list("abcdef")
li = list(orig)
sort_utils.swap(li, 0, 5)
sort_utils.swap(li, 1, 4)
sort_utils.swap(li, 2, 3)
print(li)
print("----------------------------------------")

total_tests+= 1
if list(orig)[::-1] == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")

# Test Results
print("========================================")
if tests_passed == total_tests:
    print("All lab tests PASSED!")
else:
    print("Not all tests passed...")
