#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        x = 0
        try:
            x = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
        except (ZeroDivisionError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (ValueError):
            res_list.append(0)
        finally:
            res_list.append(x)
    return (res_list)
