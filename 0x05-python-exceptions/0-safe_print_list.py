#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        while printed < x:
            print(my_list[printed], end=" ")
            printed += 1
    except IndexError:
        pass  # exit the loop if index is out of range
    print()  # add a newline after printing all elements
    return printed
