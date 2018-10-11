# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).


def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        c = b
        b = a + b
        a = c
        i = i + 1
    return a


print fibonacci(36)
# >>> 14930352
