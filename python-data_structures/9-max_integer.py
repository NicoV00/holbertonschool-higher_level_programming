#!/usr/bin/python3
def max_integer(my_list=[]):
    "Function that finds the biggest integer of a list."
    if len(my_list) == 0:
        return
    big_int = None
    for comparator in my_list:
        if big_int is None or big_int < comparator:
            big_int = comparator
    return big_int
