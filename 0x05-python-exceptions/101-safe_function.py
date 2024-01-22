#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except (ZeroDivisionError, IndexError)as e:
        print("Exception:",e)
        return None
