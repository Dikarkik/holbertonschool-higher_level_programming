#!/usr/bin/python3
# function that computes the square value
# of all integers of a matrix.


def square(num):
    return num*num


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(square, matrix[i])))
    return new_matrix
