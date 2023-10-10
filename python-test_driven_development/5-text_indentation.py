#!/usr/bin/python3
"""Created task 5"""


def text_indentation(text):
    """Print identation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = ['.', '?', ':']

    actual_line = ""

    for char in text:
        actual_line += char

        if char in special_characters:
            print(actual_line.strip())
            print()
            actual_line = ""

    if actual_line:
        print(actual_line.strip())
