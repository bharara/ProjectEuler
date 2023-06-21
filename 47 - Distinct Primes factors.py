# - Problem 47
# - Distinct Primes Factors
# 
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def numberOfDistintPrimeFactor(n):
    a = 2
    factors = set()
    while a*a<n:
        if n%a==0:
            n//=a
            factors.add(a)
        else:
            a+=1
    return len(factors) + 1


def check (i, n):
    for j in range (i, i+n):
        if numberOfDistintPrimeFactor (j) != n:
            return False
    return True

n = 4

i = 1
while not check (i, n):
    i += 1

print (i)