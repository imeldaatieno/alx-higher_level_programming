#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4, 5]
    x = 5
    while True:
        try:
            for i in my_list:
                print(i)
        except IndexError:
            print("Invalid")
