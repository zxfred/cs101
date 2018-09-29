# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.


def shift(letter):
    code = ord(letter)
    if code == 122:
        code = 97
    else:
        code = code + 1
    return chr(code)


print shift('a')
# >>> b
print shift('n')
# >>> o
print shift('z')
# >>> a
