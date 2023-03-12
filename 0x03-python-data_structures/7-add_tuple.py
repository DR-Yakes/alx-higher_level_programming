#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeroes if they have less than 2 elements
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    # Add the elements of the tuples and return a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
