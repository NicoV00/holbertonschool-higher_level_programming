#!/usr/bin/python3
"""task 10"""


class Student():
    """student class created"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "Retrieves a dict representation of a Student instance"
        if type(attrs) is list:
            data = {}
            for x in attrs:
                if hasattr(self, x):
                    data[x] = getattr(self, x)
            return data
        return (self.__dict__)
