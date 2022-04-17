#!/usr/bin/env python3

rows = 4
cols = 12

for y in range(rows):
    for x in range(cols):
        print("*", end="")
    print()


print("-------------------------------------")

for x in range(cols):
    for y in range(rows):
        print("*", end="")
    print()


print("-------------------------------------")
print("Coordinate system where 0,0 is top left.")
print("X increases as you go right.")
print("Y increases as you go down.")

# y will be 0, 1, 2, 3
for y in range(rows):
    # x will be 0, 1, 2, 3, 4, ... 10, 11
    for x in range(cols):

        point = (x, y)

        # coordinate (3, 2)
        # if x == 3 and y == 2:
        #     print("-", end="")
        # if point[0] == 3 and point[1] == 2:
        #     print("-", end="")
        if point == (3, 2):
            print("-", end="")
        else:
            print("*", end="")


    print()

print("-------------------------------------")
print("Coordinate system where 0,0 is bottom right.")
print("X increases as you go left.")
print("Y increases as you go up.")


for y in range(rows-1, -1, -1):
    for x in range(cols-1, -1, -1):
        point = (x, y)

        if point == (8, 1):
            print("-", end="")
        else:
            print("*", end="")
    print()

# (5,3)  (4,3)  (3,3)  (2,3)  (1,3)  (0,3)
# (5,2)  (4,2)  (3,2)  (2,2)  (1,2)  (0,2)
# (5,1)  (4,1)  (3,1)  (2,1)  (1,1)  (0,1)
# (5,0)  (4,0)  (3,0)  (2,0)  (1,0)  (0,0)

print("-------------------------------------")
print("Coordinate system where 0,0 is the center.")
print("X increases as you go right.")
print("Y increases as you go up.")

cols = 9
rows = 9

for y in range(rows//2, -rows//2, -1):
    for x in range(-cols//2 + 1, cols//2 + 1, 1):
        point = (x, y)

        if point == (0, 0):
            print("X", end="")
        elif y == 0:
            print("-", end="")
        elif x == 0:
            print("|", end="")
        else:
            print(" ", end="")
    print()
