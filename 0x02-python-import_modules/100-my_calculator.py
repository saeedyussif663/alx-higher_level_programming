#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    length = (len(argv)) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] != "+" and argv[2] != "-" \
and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a,b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a,b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a,b)))
        else:
            print("{} {} {} = {}".format(a, operator, b, di(a,b)))
