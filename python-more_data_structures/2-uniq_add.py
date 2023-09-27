#!/bin/usr/python3

def uniq_add(my_list=[]):
    sum = 0
    con = set(my_list)
    for x in con:
        sum += x
        return sum
