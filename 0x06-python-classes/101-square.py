#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): the size of the new square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the new size of the square."""
        if type(value) is not integer:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position of the square."""
        return self.position

    @position.setter
    def position(self, value):
        """set the position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must a be tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """find the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
