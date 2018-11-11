def iter_rabbits(n):
    current = 0
    after1 = 1
    after2 = 1
    after3 = 2
    after4 = 3
    after5 = 5
    for i in range(0, n):
        current, after1, after2, after3, after4, after5 = after1, after2, after3, after4, after5, after4 + after5 - after1
    return current


print iter_rabbits(10)
# >>> 35

s = ""
for i in range(1, 12):
    s = s + str(iter_rabbits(i)) + " "
print s
# >>> 1 1 2 3 5 7 11 16 24 35 52
