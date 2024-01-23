#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):]
    number = 0
    while True:
        try:
            for i in range(x):
                print(my_list[i], end=" ")
                number += 1
        except IndexError:
            pass
        else:
            print()
            return number
