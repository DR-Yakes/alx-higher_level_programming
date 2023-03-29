#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                raise TypeError("wrong type")
            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")
            result = elem_1 / elem_2
        except TypeError as e:
            print("wrong type")
            result = 0
        except ZeroDivisionError as e:
            print("division by 0")
            result = 0
        except IndexError as e:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
