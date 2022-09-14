#!/usr/bin/python3
"Defines a class Square"

from math import pi
class MagicClass:
    """A Magic class"""
    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2 
    
    def circumference(self):
        return 2 * pi *self.__radius



