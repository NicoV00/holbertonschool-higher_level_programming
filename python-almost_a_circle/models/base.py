#!/usr/bin/python3
"Task 0"


class Base():
    """ Base Classs """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
