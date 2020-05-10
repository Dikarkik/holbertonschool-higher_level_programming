#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda li: [list(map(lambda x: x*x, li))], matrix))
