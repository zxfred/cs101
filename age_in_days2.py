# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def calculate_days(year, month, day):
    y = 0
    m = 0
    r = 0
    while y < year:
        if isLeapYear(y):
            r = r + 366
        else:
            r = r + 365
        y = y + 1
    while m < month:
        if isLeapYear(y) and m == 2:
            r = r + 29
        else:
            r = r + daysOfMonths[m - 1]
        m = m + 1
    r = r + day
    return r

#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#    return calculate_days(year2, month2, day2) - calculate_days(year1, month1, day1)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dayIsBefore(year1, month1, day1, year2, month2, day2)
    while year1, month1, day1 != year2, month2, day2:
        day1 = day1 + 1


def nextDay(year, month, day):
    day = day + 1
    if day > 30:
        day = 1
        month = month + 1
    if month > 12:
        month = 1
        year = year + 1
    return year, month, day

def dayIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
