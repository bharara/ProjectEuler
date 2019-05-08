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

# Formula Test n
def form(a,b):
    n=0
    while isPrime[n**2+a*n+b]:
        n+=1
    return n


large=0

for a in range(-999, 1000):
  for b in range(-1000, 1001):
    j = form (a,b) 
    if j > large:
      x = a
      y = b
      large = j

print(x*y)