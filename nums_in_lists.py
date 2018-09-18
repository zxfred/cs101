# -*- coding:utf-8 -*-

# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

# Hint - "int()" turns a string's element into a number


def numbers_in_lists(string):

    # 处理空字符串
    if not string:
        return 'plz input string'

    # 转化为list
    l = []
    for num in string:
        l.append(int(num))

    i = 0
    target = 0
    r = []
    new_list = []

    while i < len(l):
        if l[i] <= target:
            new_list.append(l[i])
        else:
            if new_list:
                r.append(new_list)
            new_list = []
            r.append(l[i])
            target = l[i]
        i = i + 1
    if new_list:
        r.append(new_list)
    return r


# testcases
string = '543987'
result = [5, [4, 3], 9, [8, 7]]
print repr(string), numbers_in_lists(string) == result
string = '987654321'
result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
