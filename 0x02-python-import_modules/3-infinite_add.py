#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = (len(argv)) - 1
    if length == 0:
        print(0)
    else:
        total = 0
        i = 1
        while i <= length:
            total += int(argv[i])
            i += 1
        print(total)
