#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    args = len(sys.argv) - 1

    i = 0
    for i in range(args):
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(sub(a, b))
    elif operator == "*":
        print(mul(a, b))
    elif operator == "/":
        print(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
