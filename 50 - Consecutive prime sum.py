# - Problem 50
# - Consecutive Prime Sum
# 
# The prime 41, can be written as the sum of six consecutive primes
# This is the longest sum of consecutive primes that adds to a prime below one-hundred
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

primes = [i for i in range(n) if isPrime[i]]

consective = 1
for i in range(len(primes)):
    for d in range(consective, len(primes)-consective):
        if i > len(primes) - consective:
            break
        s = sum(primes[i:i+d])
        
        if s >= n:
            break
        if isPrime[s]:
            consective = d
            value = s
            
print (value)