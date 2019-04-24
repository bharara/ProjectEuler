n = 10001

def isPrime(a):
    for i in range (3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True

count  = 1
v = 3

while count < n:
    if isPrime(v):
        count += 1
    v += 2

print(v)