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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """Return rectangle area."""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def display(self):
        "Prints in stdout the Rectangle instance"
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        "Returns a str representation"
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        "Assigns an arg to each attribute"
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def display(self):
        "Prints in stdout the Rectangle instance"
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        "Returns a str representation"
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        "Assigns an arg to each attribute"
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
