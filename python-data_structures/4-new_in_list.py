#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylist = my_list.copy()
    if idx < 1:
        return copylist
    elif idx > len(my_list) - 1:
        return copylist
    copylist[idx] = element
    return copylist
