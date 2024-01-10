#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dict = {x: a_dictionary[x] * 2 for x in a_dictionary}
    return multiplied_dict
