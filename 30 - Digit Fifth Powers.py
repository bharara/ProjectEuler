def nsum(n):
    a = n
    ns = 0
    while n > 0:
        ns += (n%10)**5
        n //= 10
    return ns == a

n = 1000000
tot = 0
for i in range(2, n):
    if nsum(i):
        tot += i

print(tot)
