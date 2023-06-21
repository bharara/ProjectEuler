# - Problem 49
# - Prime Permutations
# 
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by $3330$, is unusual in two ways:
# (i) each of the three terms are prime, and, 
# ii) each of the 4-digit numbers are permutations of one another.
# 
# there is one other 4-digit increasing sequence. What 12-digit number do you form by concatenating the three terms in this sequence?


st = 1000
n = 10000

## Creating array where prime is 1
isPrime = [1] * n
isPrime [0] = isPrime [1] = 0
for i in range(4, n, 2):
	isPrime [i] = 0

for i in range(3, int(n**0.5)+1, 2):
	if isPrime[i]:
		for j in range (i*i, n, i):
			isPrime [j] = 0

primes = [i for i in range(st, n) if isPrime[i]]

def isPermutation(a,b,c):
  return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

for prime in primes:
	for d in range(1,10000):
		if n + d + d > 10000:
			break
		if isPrime[n+d] and isPrime[n+d+d] and isPermutation(n,n+d,n+d+d):
			print(n,n+d,n+d+d, sep = "")
