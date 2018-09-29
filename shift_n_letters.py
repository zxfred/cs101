# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
# negative or zero.


def shift_n_letters(letter, n):
    code = ord(letter)
    code = code + n
    if code > 122:
        code = code - 26
    if code < 97:
        code = code + 26
    return chr(code)


print shift_n_letters('s', 1)
# >>> t
print shift_n_letters('s', 2)
# >>> u
print shift_n_letters('s', 10)
# >>> c
print shift_n_letters('s', -10)
# >>> i
