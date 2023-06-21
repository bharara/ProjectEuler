# - Problem 37
# - Truncatable Primes
# 
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

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


def isTruncatablePrime (i):
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


total = sum(i for i in range(11,n,2) if isPrime[i] and isTruncatablePrime(i))
print(total)