# - Problem 21
# - Amicable Numbers
# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a)=b and d(b) = a, where a!=b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 100000

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

n = 10000
total = 0
for a in range(n):
    b = sumOfDivisors (a)
    if a != b and a == sumOfDivisors (b):
        total += a

print(total)