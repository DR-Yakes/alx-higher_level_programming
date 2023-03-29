#!/usr/bin/python3
class Square:
    """
    Square class with size and position attributes
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance with a given size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square instance
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square instance using the '#' character
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
