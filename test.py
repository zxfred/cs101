# encoding: utf-8

while n != 1:
    if n % 2 == 0:  # n 是偶数
        n = n / 2
        if n == 1:
            print 'stop'
    else:
        n = 3 * n + 1
        if n == 1:
            print 'stop'