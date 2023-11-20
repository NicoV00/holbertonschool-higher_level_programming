#!/usr/bin/python3
"""Task 0"""

def read_file(filename=""):
    """Read a text file"""
    with open(filename, "r") as txt:
        print(txt.read(), end="")
