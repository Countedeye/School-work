#!/usr/bin/env python3

verbose = True

swaps = []
def swap_tracker_reset():
    global swaps
    swaps = []


def swap(li, i, j):

    # Track swaps
    low = min(i, j)
    hi = max(i, j)
    swaps.append(((low, li[low]),(hi, li[hi])))

    # Code to print out the list, and swap indices and values
    if verbose:
        print(li)
        print(f"swap {low}:{li[low]} <--> {hi}:{li[hi]}")

    # You add the code to actually swap list values here

    return

if __name__ == "__main__":
    print(f'Running tests for "{__file__}"...')

    # You add your own tests here.
