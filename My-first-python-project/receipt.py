"""
File: receipt.py
Name:黃鉑翔
-------------------------
This program calculates the meal cost
and prints the result on Console.
Students will learn variables, user inputs,
and concatenation
"""


def main():
    meal = int(input('餐費:'))
    tax = float(input('稅:'))
    total = meal * (1+tax)
    print ('總和:' + str(total) + '!')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
