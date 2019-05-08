n = 1000000

a = '0'
i = 1
while len(a) <= 1000000:
    a += str(i)
    i += 1
     
def d(n):
    return int(a[n])
     
print (d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))
