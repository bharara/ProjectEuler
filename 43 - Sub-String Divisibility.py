from itertools import permutations

s = [str(i) for i in range(10)]
lst = list(permutations(s))
primes = [2,3,5,7,11,13,17]

def check(n):
    if n[0] == '0':
        return False

    for i in range (1,8):
        if int( n [i : i+3] ) % primes[i-1]:
            return False
    return True

total = 0
for i in lst:
    b = "".join(j for j in i)
    if check(b):
        print(b)
        total += int(b)

print(total)
