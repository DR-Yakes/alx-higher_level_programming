#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the result
    result = []
    # Loop over the rows of the input matrix
    for row in matrix:
        # Create a new row to store the squared values
        squared_row = []
        # Loop over the elements of the current row and square the integers
        for elem in row:
            if isinstance(elem, int):
                squared_elem = elem ** 2
                squared_row.append(squared_elem)
            else:
                squared_row.append(elem)
        # Append the squared row to the result matrix
        result.append(squared_row)
    return result
