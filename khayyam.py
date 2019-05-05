# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    result = []
    row = 0
    while row < n:
        if row == 0:
            result.append([1])
        if row == 1:
            result.append([1, 1])
        if row > 1:
            last_row = result[row - 1]
            current_row = [1]
            for index in range(len(last_row) - 1):
                current_row.append(last_row[index] + last_row[index + 1])
            current_row.append(1)
            result.append(current_row)
        row = row + 1
    return result


# For example:

# print triangle(0)
# >>> []

# print triangle(1)
# >>> [[1]]

# print(triangle(2))
# >>2 [[1], [1, 1]]

# print(triangle(3))
# >>> [[1], [1, 1], [1, 2, 1]]

print(triangle(6))
# >>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
