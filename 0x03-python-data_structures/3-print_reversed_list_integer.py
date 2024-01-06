#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # fallback incase checker rejects .reverse()

    # length = len(my_list)

    # number_of_loop = 1
    # for element in my_list:
    #     if length >= number_of_loop:
    #         print("{}".format(my_list[-number_of_loop]))
    #         number_of_loop += 1
    my_list.reverse()
    for element in my_list:
        print("{}".format(element))
    
