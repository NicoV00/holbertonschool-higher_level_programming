#!/usr/bin/python3
"""class my list"""


class MyList(list):
    """Print a list in order."""

    def print_sorted(self):
        if hasattr(self, '__str__'):
            print(sorted(self))
            return sorted(self)
