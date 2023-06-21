# - Problem 32
# - Pandigital Products
# 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.


import itertools
import math

n = 9
halfN = int(math.ceil(n/2))


def isProduct(i, j, k):
    return int("".join(i)) * int("".join(j)) == int("".join(k))


s = list(str(x+1) for x in range(n))
perms = list(itertools.permutations(s))

products = set()
for perm in perms:
    for c in range(1, halfN):
        if isProduct(perm[:c] , perm[c:halfN], perm[halfN:]):
            products.add(int("".join( perm[halfN:])))
        

print (sum(products))