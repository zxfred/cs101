# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)


def is_identity_matrix(matrix):
    if not matrix:
        return False
    row_length = len(matrix[0])
    col_length = len(matrix)

    if row_length != col_length:
        return False

    i = 0
    while i < col_length:
        j = 0
        while j < col_length:
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
            j = j + 1
        i = i + 1
    return True


# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print is_identity_matrix(matrix1)
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print is_identity_matrix(matrix2)
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print is_identity_matrix(matrix3)
# >>>False

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix4)
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print is_identity_matrix(matrix5)
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix6)
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
# >>>False

