#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, "w", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return (st)
