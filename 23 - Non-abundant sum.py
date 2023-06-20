# - Problem 23
# - Non-Abundant Sums
# 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math


def sumOfDivisors(n) : 
    result = 1
    for i in range(2,int((math.sqrt(n)))+1):
        if (n % i == 0): 
            if (i == (n/i)) : 
                result += i 
            else : 
                result += i + n//i 
          
    return result

def isAbundant(n):
    return sumOfDivisors(n) > n

limit = 28123
# lst = [False] * limit
# for i in range(12, limit-12):
#     for j in range(12, limit):
#         if isAbundant(i) a

abudants = [i for i in range(12, limit) if isAbundant(i)]
sumOfAbudants = set()

for a in abudants:
    for b in abudants:
        sumOfAbudants.add(a+b)
        if a+b > 28123:
            break
        
s = sum(n for n in range(limit) if n not in sumOfAbudants)
print (s)