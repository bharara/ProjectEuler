n = 4000000

x = 0
y = 1

s = 0

while x <= n:
    if x%2 == 0:
        s += x

    x, y = y, x+y

print(s)
