def d2b(x):
    return int(bin(x)[2:])

def reverse (n):
    return n[::-1]

def palin(n):

    n = str(n)
    l = len(n)

    if l % 2:
        return n[:l//2] == reverse(n[l//2 + 1:])
    return n[:l//2] == reverse(n[l//2:])

n = 1000000

total = 0
for i in range(1, n):
    if palin(i) and palin (d2b(i)):
        # print(i)
        total += i

print(total)