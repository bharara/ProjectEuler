# - Problem 27
# - Quadratic Primes
# 
# Euler discovered the remarkable quadratic formula: n2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 to 39
# Considering quadratics of the form: n2 + an + b where -1000 < a,b < 1000 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

n = 1000000

## Creating array where prime is 1
isPrime = [1] * n
isPrime [0] = isPrime [1] = 0
for i in range(4, n, 2):
    isPrime [i] = 0

for i in range(3, int(n**0.5)+1, 2):
    if isPrime[i]:
        for j in range (i*i, n, i):
            isPrime [j] = 0

# Formula Test n
def form(a,b):
    n=0
    while isPrime[n**2+a*n+b]:
        n+=1
    return n


large = 0
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    j = form (a,b) 
    if j > large:
      x = a
      y = b
      large = j

print(x*y, x, y, large)