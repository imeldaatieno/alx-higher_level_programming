#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4, 5]
    x = 5
     for i in range(x):
         try:
                print("{}".format(my_list[i], end="")
        except IndexError:
            print("Invalid")
