#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nicaoList = []
    for x in my_list:
        if (x % 2) == 0:
            nicaoList += [True]
        else:
            nicaoList += [False]
    return nicaoList
