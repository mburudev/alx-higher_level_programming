#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                result = 0

                if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                    try:
                        result = element_1 / element_2
                    except ZeroDivisionError:
                        print("division by 0")
                else:
                    print("wrong type")
                
                result_list.append(result)

            except IndexError:
                print("out of range")
                result_list.append(result)

    finally:
        return result_list
