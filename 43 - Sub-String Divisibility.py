# - Problem 43
# - Sub-string Divisibility

from itertools import permutations

s = [str(i) for i in range(10)]
perms = ["".join(j for j in perm) for perm in permutations(s)]
primes = [2,3,5,7,11,13,17]

def check(n):
    if n[0] == '0':
        return False

    for i in range (7):
        if int( n [i+1 : i+4] ) % primes[i]:
            return False
    return True

total = sum(int(perm) for perm in perms if check(perm))
print(total)