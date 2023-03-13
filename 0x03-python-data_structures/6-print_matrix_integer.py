#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for inner_list in matrix:
            for i in range(0, len(inner_list)):
                if i == len(inner_list) - 1:
                    print("{:d}".format(inner_list[i]))
                else:
                    print("{:d}".format(inner_list[i]), end=" ")
