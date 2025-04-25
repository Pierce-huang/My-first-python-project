"""
File: DoubleBeepers.py
Name:黃鉑翔
-------------------------------
"""

from karel.stanfordkarel import *


def main():
    #Karel will double the beepers
    move()
    double_beepers()
    put_beepers_back()
    Karel_goes_home()


def double_beepers():
    while on_beeper():
        #(1,2) facing East.
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        #(1,3) facing East.
        turn_around()
        move()
        #(1,2) facing West.
        turn_around()


def  put_beepers_back():
    #(1,2) facing East.
    move()
    while on_beeper():
        #(1,3) facing East.
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        #(1,2) facing West.
        turn_around()
        move()


def Karel_goes_home():
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    #Turn left twice.
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
