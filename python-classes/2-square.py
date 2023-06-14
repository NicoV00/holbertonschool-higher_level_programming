#!/usr/bin/python3
""" Python """


class Square:
    """ Class: Square """
    __size = 0

    def __init__(self, size=0):
        """Init size of square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
