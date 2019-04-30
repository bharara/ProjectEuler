def collnum(i):
    if i in d:
        return d[i]
    else:
        if i%2:
            j = 3*i + 1
        else:
            j = i//2

        k = collnum(j) + 1
        d[i] = k
        return k


n = 1000000
d = {
    2: 1
}

large = 0
ans = 0
for i in range (2, n):
    c = collnum(i)
    if c > large:
        large = c
        ans = i

print(large, ans)
