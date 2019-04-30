def factorial(n):
    if n == 2:
        return 2
    return n * factorial (n - 1)


n = 100
s = 0
for i in list(str(factorial(n))):
    s += int(i)

print(s)
