#!/usr/bin/python3
def best_score(a_dictionary):
    # Initialize the best score to None and the best key to an empty string
    best_score = None
    best_key = ""
    # Iterate over the items in the dictionary
    for key, value in a_dictionary.items():
        # If the value is greater than the current best score, update
        if best_score is None or value > best_score:
            best_score = value
            best_key = key
    # Return the best key
    return best_key if best_score is not None else None
