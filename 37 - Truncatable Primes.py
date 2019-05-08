n = 1000000

## Creating array where prime is 1
isPrime = [1] * n
isPrime [1] = 0
for i in range(4, n, 2):
    isPrime [i] = 0

for i in range(3, int(n**0.5)+1, 2):
    if isPrime[i]:
        for j in range (i*i, n, i):
            isPrime [j] = 0


def isAllPrime (i):
    j = 10
    while j <= 100000:
        if not isPrime[i%j]:
            return False
        j *= 10

    while j > 1:
        if not isPrime[i//j]:
            return False
        j //= 10
    return True


total = 0
for i in range(11,n):
    if isPrime[i]:
        if isAllPrime(i):
            total += i
    n += 2

print(total)