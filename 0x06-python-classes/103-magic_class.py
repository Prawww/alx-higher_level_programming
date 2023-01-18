#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius):
        """Initialize a MagicClass

        Args:
            radius (float or int): the radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """"Return area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of the MagicClass."""
        return (self.__radius * 2 * math.pi)
