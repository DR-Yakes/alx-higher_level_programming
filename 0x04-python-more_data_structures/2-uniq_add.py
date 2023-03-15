#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_ints = set()
    for elem in my_list:
        if isinstance(elem, int):
            unique_ints.add(elem)
    # Return the sum of the unique integers
    return sum(unique_ints)
