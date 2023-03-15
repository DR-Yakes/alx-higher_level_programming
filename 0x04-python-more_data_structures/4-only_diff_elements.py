#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a new set to store the difference of the two sets
    difference = set()

    for elem in set_1:
        if elem not in set_2:
            difference.add(elem)

    for elem in set_2:
        if elem not in set_1:
            difference.add(elem)

    return difference
