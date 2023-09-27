#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    con = set(my_list)
    for x in con:
        total += x
    return total
