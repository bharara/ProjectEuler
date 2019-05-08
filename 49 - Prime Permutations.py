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

prime = [i for i in range(st, n) if isPrime[i]]

#print(prime)

def rotate(a,b,c):
  return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

for n in prime:
  for d in range(1,10000):
    if n + d + d >10000:
      break
    if isPrime[n+d] and isPrime[n+d+d] and rotate(n,n+d,n+d+d):
      print(n,n+d,n+d+d, sep = "")
