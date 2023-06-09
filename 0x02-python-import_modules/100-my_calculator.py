#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    args = len(sys.argv) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    i = 0
    for i in range(args):
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
