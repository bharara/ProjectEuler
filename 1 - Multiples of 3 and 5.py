# - Problem 1
# - Multiples of 3 or 5
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

import math

limit = 1000

# Sum of products in arthemtic progression
def sum_ap(a, limit=limit):
    n =  math.floor((limit-1) / a)
    return (n * (n+1)) // 2 * a

print(sum_ap(3) + sum_ap(5) - sum_ap(15))