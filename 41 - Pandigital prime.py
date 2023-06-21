# - Problem 41
# - Pandigital Prime
# 
# What is the largest n-digit pandigital prime that exists?

from math import sqrt
from itertools import permutations

def isPrime (x):
	if x == 2: return True
	if x % 2 == 0: return False

	for i in range(3,int(sqrt(x)+1), 2):
		if x % i == 0:
			return False

	return True

val = 0
for i in range (9,1,-1):
	s = "".join([str(x+1) for x in range(i)])
	p = list(permutations(s))

	for j in p:
		k = int("".join(j))
		if isPrime(k):
			val = k

	if val != 0: ## If a value if found, it must be largest, break
		break

print(val)