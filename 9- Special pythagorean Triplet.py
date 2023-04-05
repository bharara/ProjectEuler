# - Problem 9
# - Special Pythagorean triplet
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

n = 1000

# We know
# a + b + c = n
# a2 + b2 = c2
# 
# Putting value of c
# a2 + b2 = (n - a - b)2
# a2 + b2 = n2 + a2 + b2 + 2ab - 2na - 2nb
# 2nb - 2ab = n2 - 2na
# 2b (n - a) = n (n - 2a)
# b = [n (n - 2a)] / [2 (n-a)]

for a in range (1, n//2):
    b = (n * (n - 2 * a)) / (2 * (n - a))
    if b.is_integer():
        c = n - a - b
        prod = a*b*c

print (prod)