from math import sqrt
from itertools import permutations

def isPrime (x):
	if x == 2: return True
	if x % 2 == 0: return False

	for i in range(3,int(sqrt(x)+1), 2):
		if x % i == 0:
			return False

	return True


for i in range (2,10):
	s = "".join([str(x+1) for x in range(i)])
	p = list(permutations(s))

	for j in p:
		k = int("".join(j))
		if isPrime(k):
			val = k

print(k)