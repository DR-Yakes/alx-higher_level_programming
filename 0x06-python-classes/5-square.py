#!/usr/bin/python3
class Square:
    """
    This class defines a square by a private instance
    attribute called size. The size represents the length
    of each side of the square. It also has a property
    setter and getter for size. Instantiation of this class
    takes an optional parameter called size with type and
    value verification. It also has a public method that
    calculates the area of the square and prints the square
    with '#' characters.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            The size of the square (int).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The length of each side of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            The area of the square (int).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' characters to stdout.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
