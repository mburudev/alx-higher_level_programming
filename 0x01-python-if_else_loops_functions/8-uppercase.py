#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print(char, end="")
    print()
