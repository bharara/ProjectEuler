# - Problem 24
# - Lexicographic Permutations
# 
# A permutation is an ordered arrangement of objects.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# What is the millionth lexicographic permutation of the digits 0 to 9.

from itertools import permutations
from math import factorial

def permutation(lst):

    if len(lst) == 0: return []
    if len(lst) == 1: return [lst]

    l = []
    for i in range(len(lst)):
        current =  lst[i]
        remList = lst[:i] + lst[i+1:]

        for perm in permutation(remList):
            l.append([current] + perm)
    return l


digits = "0 1 2 3 4 5 6 7 8 9".split()
n = 1000000

# perms = list(permutations(digits))
# perms = list(permutation(digits))
# print(perms[n-1])

ans = []
rem = n-1
for i in range(len(digits)-1, -1, -1):
    div = factorial(i)
    current_i = rem // div
    rem = rem % div

    print (i, div, current_i, rem, digits[current_i], digits)
    ans.append(digits.pop(current_i))

print ("".join(ans))