"""
File: my_smaller.py
Name:黃鉑翔
-------------------------
This program implements a my_smaller function
which takes 2 arguments and outputs the
smaller one
"""


def main():
    """
    Call my_smaller function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)
    ans = my_add(n1, n2)
    print(ans)


def my_add(n1, n2):
    ans = n1 + n2
    return ans


def my_smaller(n1, n2):
    """
    :param n1:
    :param n2:
    :return:
    """
    if n1 < n2:
        return n1
    elif n1 > n2:
        return n2
    else:
        return n2


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
