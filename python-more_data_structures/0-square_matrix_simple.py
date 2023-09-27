#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        squared = []
        for element in x:
            squared.append(element*element)
        new_matrix.append(squared)
    return new_matrix
