def rotate(n):
    rot = []
    m = str(n)
    counter = 0
    while counter < len(str(n))-1:
        m = m[1:] + m[0]
        rot.append(int(m))
        counter += 1
    return rot

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
    rotation = rotate (i)

    for j in rotation:
      if isPrime [j]:
        c += 1
      else:
        break

    if c == len(rotation):
      count += 1

print(count)

