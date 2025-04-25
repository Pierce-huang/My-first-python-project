"""
File: find_max.py
Name: 黃鉑翔
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('找最大值')
    data = int(input('數據:'))
    if data == EXIT:
        print('沒有資料: (')
    else:
        maximum = data
        while True:
            data = int(input('數據:'))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print('最大值'+str(maximum))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
