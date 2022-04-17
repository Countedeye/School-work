#!/usr/bin/env python3

import sort_utils
from selection import selection_sort


tests_passed = 0
total_tests = 0

test_name = "Test 1 - a"
print(f"---- {test_name} ----------------------------")
orig = li = [12, 7, 32, 5, 16, 4]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[12, 7, 32, 5, 16, 4]",
    "swap 0:12 <--> 5:4",
    "[4, 7, 32, 5, 16, 12]",
    "swap 1:7 <--> 3:5",
    "[4, 5, 32, 7, 16, 12]",
    "swap 2:32 <--> 3:7",
    "[4, 5, 7, 32, 16, 12]",
    "swap 3:32 <--> 5:12",
    "[4, 5, 7, 12, 16, 32]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [4, 5, 7, 12, 16, 32]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 1 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 12), (5, 4)), ((1, 7), (3, 5)), ((2, 32), (3, 7)), ((3, 32), (5, 12))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 2 - a"
print(f"---- {test_name} ----------------------------")
orig = li = [88, 98, 43, 11, 78, 19, 27]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[88, 98, 43, 11, 78, 19, 27]",
    "swap 0:88 <--> 3:11",
    "[11, 98, 43, 88, 78, 19, 27]",
    "swap 1:98 <--> 5:19",
    "[11, 19, 43, 88, 78, 98, 27]",
    "swap 2:43 <--> 6:27",
    "[11, 19, 27, 88, 78, 98, 43]",
    "swap 3:88 <--> 6:43",
    "[11, 19, 27, 43, 78, 98, 88]",
    "swap 5:98 <--> 6:88",
    "[11, 19, 27, 43, 78, 88, 98]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [11, 19, 27, 43, 78, 88, 98]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 2 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 88), (3, 11)), ((1, 98), (5, 19)), ((2, 43), (6, 27)), ((3, 88), (6, 43)), ((5, 98), (6, 88))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 3"
print(f"---- {test_name} ----------------------------")
orig = li = [123, 456, 267, 96, 142, 387]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[123, 456, 267, 96, 142, 387]",
    "swap 0:123 <--> 3:96",
    "[96, 456, 267, 123, 142, 387]",
    "swap 1:456 <--> 3:123",
    "[96, 123, 267, 456, 142, 387]",
    "swap 2:267 <--> 4:142",
    "[96, 123, 142, 456, 267, 387]",
    "swap 3:456 <--> 4:267",
    "[96, 123, 142, 267, 456, 387]",
    "swap 4:456 <--> 5:387",
    "[96, 123, 142, 267, 387, 456]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [96, 123, 142, 267, 387, 456]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 3 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 123), (3, 96)), ((1, 456), (3, 123)), ((2, 267), (4, 142)), ((3, 456), (4, 267)), ((4, 456), (5, 387))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


# Test Results
tests_failed = total_tests - tests_passed
print("========================================")
if tests_failed == 0:
    print("All lab tests PASSED!")
else:
    print(f"{tests_failed} tests failed...")
