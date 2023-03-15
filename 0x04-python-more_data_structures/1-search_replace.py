#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the result
    result = []
    # Loop over the elements of the input list
    for elem in my_list:
        if elem == search:
            result.append(replace)
        else:
            result.append(elem)

    return result
