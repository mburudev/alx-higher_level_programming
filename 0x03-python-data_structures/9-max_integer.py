#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest_number = my_list[0]
    for number in my_list:
        if number > largest_number:
            largest_number = number
    return largest_number
