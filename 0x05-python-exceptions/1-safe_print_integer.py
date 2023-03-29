#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()  # add a newline after printing
        return True
    except (TypeError, ValueError):
        return False
