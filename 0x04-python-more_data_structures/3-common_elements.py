#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create a new set to store common elements
    common = set()

    for elem in set_1:
        if elem in set_2:
            common.add(elem)

    return common
