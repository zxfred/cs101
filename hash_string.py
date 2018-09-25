# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


def hash_string(keyword, buckets):
    pointer = 0
    for letter in keyword:
        # This solution is slower when the final point is too big
        # pointer += ord(letter)
        pointer = (pointer + ord(letter)) % buckets
    return pointer % buckets


print hash_string('a', 12)
# >>> 1

print hash_string('b', 12)
# >>> 2

print hash_string('a', 13)
# >>> 6

print hash_string('au', 12)
# >>> 10

print hash_string('udacity', 12)
# >>> 11
