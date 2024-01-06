#!/usr/bin/python3

def no_c(my_string):
    length_of_str = len(my_string)
    new_string = []
    for char in range(0, length_of_str):
        if my_string[char] != "c" and my_string[char] != "C":
            new_string.append(my_string[char])
        else:
            continue
    new_string = "".join(new_string)
    return new_string
