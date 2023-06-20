# - Problem 19
# - Counting Sundays
# 
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

def daysInMonth(m,y):
    if m==4 or m==6 or m==9 or m==11: return 30
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12: return 31
    if isLeap(y): return 29
    return 28

def isLeap (y):
    return not y%4 or (y%100 and not y%400)

start = date(1901, 1, 1)
end = date(2000, 12, 31)
weKnow = date(1900, 1, 1)

# 1st Jan 1901
day = (start - weKnow).days % 7 + 1

count=0

# First Year (may be partial)
for m in range(start.month - 1, 12):
    if day%7 == 0:
        count += 1
    day += daysInMonth(m+1,start.year)


#  Remaining Years
for y in range (start.year+1, end.year):
    for m in range(12):
        if day%7 == 0:
            count += 1
        day += daysInMonth(m+1,start.year)


# Last Year (may be partial)
for m in range(end.month):
    if day%7 == 0:
        count += 1
    day += daysInMonth(m+1,start.year)

print(count)
