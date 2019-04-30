import math

def numfac(num):
    n=1
    fac=0
    while n*n<=num:
        if num%n==0: fac+=2
        n+=1
    return fac


n = 500
for i in range(1,1000000):
	T = i * (i+1) // 2
	if i%2 == 0:
		c = numfac (i//2) * numfac (i+1)
	else:
		c = numfac (i) * numfac ((i+1)//2)

	if c >= n:
		break

print(T)