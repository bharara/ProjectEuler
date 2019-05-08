from random import randint

def shuffle ():
    return str(randint (0, 9))

def misMatch (s):
    miss = 0
    for i in range(k):
        hit = 0
        for j in range(n):
            if s[j] == array[i][j]:
                hit += 1
    

        miss += abs(hit - hits[i])
    return miss


array = []
hits = []

array = [5616185650518293,
3847439647293047,
5855462940810587,
9742855507068353,
4296849643607543,
3174248439465858,
4513559094146117,
7890971548908067,
8157356344118483,
2615250744386899,
8690095851526254,
6375711915077050,
6913859173121360,
6442889055042768,
2321386104303845,
2326509471271448,
5251583379644322,
1748270476758276,
4895722652190306,
3041631117224635,
1841236454324589,
2659862637316867]

k = len(array)

for i in range(k):
    array[i] = list(str(array[i]))

hits = [2, 1, 3, 3, 3, 1, 2, 3, 1, 2, 3,1, 1, 2, 0, 2, 2, 3, 1, 3, 3, 2]
    
n = len(array[0])


currentS = ''
for i in range(n):
    currentS += shuffle()

wait = 0
error = misMatch (currentS)
lastError = error

while (error != 0):
    for i in range(n):
        previousDigit = currentS[i]
        currentS = currentS[:i] + shuffle() + currentS[i+1:]

        newError = misMatch(currentS)

        if (newError <= error):
            error = newError
        else:
            currentS = currentS[:i] + previousDigit + currentS[i+1:]


    if error == lastError:
        wait += 1

        if wait == 30:
            r = randint(0,n-1)
            currentS = currentS[:r] + shuffle() + currentS[r+1:]
            error = misMatch(currentS)
            wait = 0
    else:
        wait = 0
        lastError = error

print(currentS)