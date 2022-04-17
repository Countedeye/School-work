#!/usr/bin/env python3

import time

ROWS = 12
COLS = 24

encountered_nibble = False

#        TAIL                  HEAD
snake = [(1,1), (2,1), (2,2), (2,3), (2,4), (3,4)]

nibbles = [(15, 7)]

# u d l r
# directions = ["u", "u", "r", "r", "x", "r", "r", "d", "d", "x", "x", "x"]
directions = []

def direct_snake(d, num=1):
    for i in range(num):
        directions.append(d)

direct_snake("r", 18)
direct_snake("d", 5)
direct_snake("l", 12)
direct_snake("u", 1)
direct_snake("r", 6)
direct_snake("u", 7)



def clear_screen():
    print("\n"*28)

def move_snake(d):

    global encountered_nibble
    if encountered_nibble:
        encountered_nibble = False
    else:
        snake.pop(0)

    head = snake[-1]

    if d == "u":
        snake.append( (head[0], head[1]-1) )
    elif d == "r":
        snake.append( (head[0]+1, head[1]) )
    elif d == "d":
        snake.append( (head[0], head[1]+1) )
    elif d == "l":
        snake.append( (head[0]-1, head[1]) )
    else:
        return

def check_for_nibbles():
    global encountered_nibble
    if snake[-1] in nibbles:
        nibbles.remove(snake[-1])
        encountered_nibble = True


def draw_board():
    for y in range(ROWS):
        for x in range(COLS):

            point = (x, y)

            if point == snake[-1]:
                print("@", end="")
            elif point in snake:
                print("*", end="")
            elif point in nibbles:
                print("o", end="")
            elif y == 0 or y == ROWS -1:
                print("-", end="")
            elif x == 0 or x == COLS -1:
                print("|", end="")
            else:
                print(" ", end="")

        print()


# Main game loop
for d in directions:
    clear_screen()
    draw_board()
    time.sleep(.2)
    move_snake(d)
    # check_for_collisions()
    check_for_nibbles()




# -------------
# |           |
# |           |
# |           |
# |           |
# -------------
