#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    i = 0
    while i < length:
        length_of_inner = len(matrix[i])
        j = 0
        while j < length_of_inner:
            print(matrix[i][j], end= " ")
            j += 1
        print("")
        i += 1