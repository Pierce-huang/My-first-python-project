"""
File: CheckerboardKarel.py
Name:黃鉑翔
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


"""目前情況:可正常執行偶數邊長，但執行奇數邊長會改成對齊排列，必須先斜向上走一格才可開始。必須分辨奇數、偶數情形！！！"""


def main():
    """
    pre-condition:
    post-condition:
    """
    while front_is_clear():
        complete_one_street()
        move_to_next_street_1()
        complete_one_street()
        move_to_next_street_2()
#8*1
    if not front_is_clear():
        turn_left()
        """put_beeper()"""
        while front_is_clear():
            put_beeper()
            if front_is_clear():
                move()
                if front_is_clear():
                    move()
                    """for i in range(3):
                        if not front_is_clear():
                            turn_left()
                    put_beeper()"""


def complete_one_street():
    """
    Karel will complete one street from left to right.
    """
    if front_is_clear():
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()


def move_to_next_street_1():
    """
    Karel is on the far right, he will move up one space to the next street, facing left.
    """
    #if front_is_clear():
    if on_beeper():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            move()
    else:
        turn_left()
        if front_is_clear():
            move()
            turn_left()


def move_to_next_street_2():
    """
    Karel is on the far left, he will move up one space to the next street, facing right.
    """
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def turn_right():
    """
    Turn left thrice.
    """
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
