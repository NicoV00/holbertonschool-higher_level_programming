#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    if (my_list):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                elements += 1
            except (ValueError, TypeError):
                pass
    print()
    return (elements)
