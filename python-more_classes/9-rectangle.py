#!/usr/bin/python3
"""Task 2"""


class Rectangle():
    """Defines rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    def __str__(self):
        """string"""
        output_str = ""
        if self.__width == 0 or self.__height == 0:
            return output_str
        for i in range(self.__height):
            for _ in range(self.__width):
                output_str += str(self.print_symbol)
            if i != self.__height - 1:
                output_str += "\n"
        return output_str

    def __repr__(self):
        """string representation"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """print bye"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        "height"
        return self.__height

    @property
    def width(self):
        "width"
        return self.__width

    @height.setter
    def height(self, value):
        "height"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        "width"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def bigger_or_equal(rect_1, rect_2):
        """return bigger area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    def square(self, size=0):
        """square"""
        return Rectangle(size, size)
