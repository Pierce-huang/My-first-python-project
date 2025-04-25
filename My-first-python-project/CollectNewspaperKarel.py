"""
File: CollectNewspaperKarel.py
Name: 黃鉑翔
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is in the northwest of the house.
    post-condition:Karel and the newspaper are in the northwest of the house. Karel puts down the newspaper,facing East.
    """
    move_to_the_newspaper()
    take_the_newspaper_home_and_read()


def move_to_the_newspaper():
    """
    pre-condition:Karel is in the northwest of the house.
    post-condition:Karel is on the beeper,facing East.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def take_the_newspaper_home_and_read():
    """
    pre-condition:Karel is on the beeper,facing East.
    post-condition:Karel and the newspaper are in the northwest of the house. Karel puts down the newspaper,facing East.
    """
    pick_beeper()
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Turn left thrice.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Turn left twice.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
