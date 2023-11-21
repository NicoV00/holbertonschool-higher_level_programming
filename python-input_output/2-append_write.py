#!/usr/bin/python3
"""task 2"""


def append_write(filename="", text=""):
    """appends a string at end of file"""
    with open(filename, "a", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return (st)
