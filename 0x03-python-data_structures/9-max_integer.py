#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = None
    first_iteration = True
    if len(my_list) == 0:
        return max_value
    else:
        for value in my_list:
            if first_iteration:
                max_value = value
                first_iteration = False
            else:
                if value > max_value:
                    max_value = value
    return max_value
