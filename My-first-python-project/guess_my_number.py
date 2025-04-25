"""
File: guess_my_number.py
Name: 黃鉑翔
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
    print('猜 0-99')
    while True:
        guess = int(input('you guess:'))
        if guess == SECRET:
            break
        elif guess > SECRET:
            print('too high')
        else:
            print('too low')
    print('Congrats! The answer: '+str(SECRET))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
