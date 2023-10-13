#!/usr/bin/python3
"""task 1"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        "Height getter"
        return self.__height

    @height.setter
    def height(self, value):
        "Height setter"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        "Width getter"
        return self.__width

    @width.setter
    def width(self, value):
        "Width setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.x_valid(x)
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.y_valid(y)
        self.__y = y
