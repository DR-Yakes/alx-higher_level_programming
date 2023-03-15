#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the list of keys in the dictionary and sort it
    keys_list = list(a_dictionary.keys())
    keys_list.sort()

    # Loop over the sorted keys and print each key-value pair
    for key in keys_list:
        value = a_dictionary[key]
        print(key + ':', value)
