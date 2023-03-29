#!/usr/bin/python3
class Square:
    """
    This class defines a square by a private instance
    attribute called size. The size represents the length
    of each side of the square. Instantiation of this class
    requires a parameter called size with no type or value
    verification.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The length of each side of the square.
        """
        self.__size = size
