#!/usr/bin/python3
"""task 8"""


BaseGeometry = __import__("7-base_geomtry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """init rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width =  width
        self.__height =  height
