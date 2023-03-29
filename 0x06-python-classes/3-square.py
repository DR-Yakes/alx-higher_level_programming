#!/usr/bin/python3
class Square:
    """
    This class defines a square by a private instance
    attribute called size. The size represents the length
    of each side of the square. Instantiation of this class
    takes an optional parameter called size with type and
    value verification. It also has a public method that
    calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int, optional): The length of each side of the square.
                Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            The area of the square (int).
        """
        return self.__size ** 2
