#!/usr/bin/python3
"""class my list"""


class Mylist(list):
    """Print list"""
    def print_sorted(self):
        print(sorted(self))
