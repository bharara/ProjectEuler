# - Problem 6
# - Sum square difference
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square_of_sum(n):
    s = n*(n+1)/2
    return s*s

def sum_of_square(n):
    return n*(n+1)*(2*n+1)/6

n = 100

print(int(abs(square_of_sum(n)-sum_of_square(n))))
