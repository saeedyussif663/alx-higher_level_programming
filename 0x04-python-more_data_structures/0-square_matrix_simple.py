#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    final = []
    for item in matrix:
        square = [i*i for i in item]
        final.append(square)
    return final