# - Problem 30
# - Digit Fifth Powers
# 
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def nsum(n, p):
    return sum(int(i)**p for i in list(str(n))) == n

n = 1000000
tot = sum(i for i in range(2, n) if nsum(i, 5))

print(tot)