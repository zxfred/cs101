# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(square):

    if not square:
        return True

    row_length = len(square[0])
    column_length = len(square)

    if row_length != column_length:
        return False

    i = 0
    while i < column_length:
        j = 0
        while j < column_length:
            if square[i][j] != square[j][i]:
                return False
            j = j + 1
        i = i + 1
    return True


print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]])
# >>> False

print symmetric([[1, 2],
                 [2, 1]])
# >>> True

print symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]])
# >>> False

print symmetric([[1, 2, 3],
                 [2, 3, 1]])
# >>> False