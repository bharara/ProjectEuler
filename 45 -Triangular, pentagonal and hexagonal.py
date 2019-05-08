from math import sqrt
def isPentagonal(x):
	return (sqrt(1 + 24 * x) % 6) == 5

def isHexagonal (x):
	return (sqrt(8*x + 1) + 1) % 4 == 0

def T (i):
	return i * (i+1) // 2

n = 100000

for i in range (286, n):
	t = T(i)
	if isPentagonal (t) and isHexagonal (t):
		print(t)
