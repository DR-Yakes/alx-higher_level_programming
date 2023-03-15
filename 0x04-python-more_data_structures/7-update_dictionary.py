#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, replace its value with the new value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add a new key-value pair to the dictionary
        a_dictionary.update({key: value})
