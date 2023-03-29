#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    i = 0
    try:
        while printed < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                printed += 1
            i += 1
    except IndexError:
        pass  # exit the loop if index is out of range
    print()  # add a newline after printing all elements
    return printed
