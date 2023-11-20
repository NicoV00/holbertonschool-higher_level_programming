#!/usr/bin/python3
"""task 6"""


class BaseGeometry:
    """class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greter than 0")
