#!/usr/bin/python3

def safe_print_integer_err(value):
    i = None
    try:
        print("{:d}".format(value))
        i = True
    except ValueError as e:
        i = False
        print(e)
    finally:
        return i