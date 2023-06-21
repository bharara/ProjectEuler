# - Problem 35
# - Circular Primes
# 
# How many circular primes are there below one million?

def getRotation(n):
	rotations = []
	m = str(n)
	for i in range(len(m) - 1):
		m = m[1:] + m[0]
		rotations.append(int(m))
	return rotations

def areAllPrimes(arr):
	for item in arr:
		if not isPrime[item]:
			return False
	return True

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

count = 0
for i in range(2,n):
	if isPrime [i]:
		c = 0
		rotations = getRotation (i)
		
		if areAllPrimes(rotations):
			count += 1

print(count)

