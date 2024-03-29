#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the result
    result = {}
    # Iterate over the items in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and add it to the result dictionary
        result[key] = value * 2
    # Return the result dictionary
    return result
