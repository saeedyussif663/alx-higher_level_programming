#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = (len(argv)) - 1
    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
        print(f"{length}: {argv[length]}")
    else:
        print(f"{length} arguments:")
        i = 1
        while i <= length:
            print(f"{i}: {argv[i]}")
            i += 1
