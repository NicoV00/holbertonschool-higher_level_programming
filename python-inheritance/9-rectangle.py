#!/usr/bin/python3
"""task 9"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""
    def __init__(self, width, height):
        """Init Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        """return area"""
        return self.width * self.height

    def __str__(self):
        """rectangle"""
        return f"[Rectangle] {self.width}/{self.height}"
