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


def dayOfMonth(year, month):
    result = daysOfMonths[month - 1]
    if isLeapYear(year) and month == 2:
        result = result + 1
    return result


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert dayIsBefore(year1, month1, day1, year2, month2, day2)
    while dayIsBefore(year1, month1, day1, year2, month2, day2):
        day1 = day1 + 1


def nextDay(year, month, day):
    if day < dayOfMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


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
