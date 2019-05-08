n = 1000

x = 0
y = 1

i = 0
while True:
    if len(str(x)) >= n:
        print(i)
        break
    i += 1
    x, y = y, x+y

