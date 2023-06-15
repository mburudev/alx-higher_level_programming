#!/usr/bin/python3
a = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - a)), end="")
    a = 32 if a == 0 else 0
