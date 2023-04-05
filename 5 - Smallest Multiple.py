# - Problem 5
# - Smallest multiple
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 

n = 20

from math import gcd

a = list(range(2,n+1))
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
    
print(lcm)