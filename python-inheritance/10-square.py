#!/usr/bin/python3
"""task 10"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """init square"""
        self.integer_validator("size", size)
        self.size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Return area"""
        return self.size ** 2
