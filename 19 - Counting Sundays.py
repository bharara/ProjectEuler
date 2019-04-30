from datetime import date

def daymon(m,y):
    if m==4 or m==6 or m==9 or m==11:
        return 30
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    if isLeap(y): return 29
    return 28

def isLeap (y):
    if y%4:
        return False
    if y%400:
        if y%100:
            return True
        return False
    return True


start = date(1901, 1, 1)
end = date(2000, 12, 31)
weKnow = date(1900, 1, 1)

day = (start - weKnow).days % 7 + 1

count=0

for m in range(start.month - 1, 12):
    for d in range(start.day - 1, daymon(m+1,start.year)):
        if day%7==0 and d==0:
            count+=1
        day+=1

for y in range (start.year+1, end.year):
    for m in range(12):
        for d in range(daymon(m+1,y)):
            if day%7==0 and d==0:
                count+=1
            day+=1

for m in range(end.month):
    for d in range(end.day):
        if day%7==0 and d==0:
            count+=1
        day+=1

print(count)
