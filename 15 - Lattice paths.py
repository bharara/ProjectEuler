# - Problem 15
# - Lattice Paths
# 
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20x20 grid?


# Problems boils down to how many ways we can arrange 40 options (2 steps, 20x20 grid) into 20 columns
from math import factorial

def nCr(n,r):
    return factorial(n) // factorial(r) // factorial(n-r)

n = 20
print (nCr(2*n, n)) 
