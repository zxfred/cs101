# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(second):
    rest = second - int(second)
    second = int(second)
    h = second / 3600
    second = second % 3600
    m = second / 60
    s = second % 60 + rest
    if h == 1:
        h = str(h) + ' hour'
    else:
        h = str(h) + ' hours'
    if m == 1:
        m = str(m) + ' minute'
    else:
        m = str(m) + ' minutes'
    if s == 1:
        s = str(s) + ' second'
    else:
        s = str(s) + ' seconds'
    return h + ', ' + m + ', ' + s


def convert_to_b(num, unit):
    list = ['kb', 'kB', 'Mb', 'MB', 'Gb', 'GB', 'Tb', 'TB']
    i = 0
    for e in list:
        if e == unit:
            result = 2 ** (10 * (i / 2 + 1))
            if i % 2 == 0:
                return result * num * 1.0
            else:
                return result * 8 * num * 1.0
        i = i + 1


def download_time(file_size, file_unit, bw, bw_unit):
    second = convert_to_b(file_size, file_unit) / convert_to_b(bw, bw_unit)
    return convert_seconds(second)


print download_time(1024, 'kB', 1, 'MB')
# >>> 0 hours, 0 minutes, 1 second

print download_time(1024, 'kB', 1, 'Mb')
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13, 'GB', 5.6, 'MB')
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13, 'GB', 5.6, 'Mb')
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10, 'MB', 2, 'kB')
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10, 'MB', 2, 'kb')
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(1, 'kB', 3, 'MB')