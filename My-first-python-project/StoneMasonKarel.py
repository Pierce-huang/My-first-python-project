"""
File: StoneMasonKarel.py
Name:黃鉑翔
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is at (1,1),facing East.
    post-condition:Karel is at (x,1),facing East.('x' is the rightmost abscissa ) And all pillars are filled with beepers.
    """
    #Repair one pillar
    while front_is_clear():
        turn_left()
        while front_is_clear():
            if on_beeper():
                move()
            else:
                put_beeper()
                move()
        if not on_beeper():
            put_beeper()
        turn_around()

        for i in range(4):
            move()
    #Move to next pillar
        turn_left()
    
        if front_is_clear():
            for i in range(4):
                move()
    if not turn_left():
        while front_is_clear():
            if on_beeper():
                move()
            else:
                put_beeper()
                move()
        if not on_beeper():
            put_beeper()
        turn_around()

        for i in range(4):
            move()
        turn_left()

        if front_is_clear():
            for i in range(4):
                move()


def turn_around():
    """
    Turn left twice.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
