#!/usr/bin/python3
for letter in range(122, 64, -1):
    print("{}{}".format(chr(letter), chr(letter-32)), end="")
