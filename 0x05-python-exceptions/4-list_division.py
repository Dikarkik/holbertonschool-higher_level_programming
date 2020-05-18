#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    index = 0
    division = 0
    new_list = []
    for index in range(list_length):
        division = 0
        try:
            division = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(division)
    return new_list
