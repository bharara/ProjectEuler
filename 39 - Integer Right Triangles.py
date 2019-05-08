def numberOfPairs (x):
    count = 0
    for a in range (1, x//2):
        for b in range(a, x//2):
            c = (a*a + b*b) ** (0.5)
            if a + b + c == x:
                count += 1
                break
    return count

n = 1000

large = 0
for i in range(12,n,12):
    j = numberOfPairs (i)
    if j > large:
        large = j

print(large)
