n = 1000000
k = 10000

## Creating array where prime is 1
isPrime = [1] * n
isPrime [0] = isPrime [1] = 0
for i in range(4, n, 2):
    isPrime [i] = 0

for i in range(3, int(n**0.5)+1, 2):
    if isPrime[i]:
        for j in range (i*i, n, i):
            isPrime [j] = 0

prime = [i for i in range(n) if isPrime[i]]


d = 0
for st in range(k):
	for end in range (st+d, k):
		s = sum(prime [st:end] )
		if s > 1000000:
			break
		if isPrime[s]:
			val = s
			d = end - st

print (val)
		