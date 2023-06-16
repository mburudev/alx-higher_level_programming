#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = f"{my_list[::-1]}"
    for i in reversed_list:
        if i != ',' and i != '[' and i != ']' and i != ' ':
            print(i)
