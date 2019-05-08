from math import sqrt

def isPentagonal(x):
	return (sqrt(1 + 24 * x) % 6) == 5

def P (i):
	return i * (3 * i - 1) / 2



n = 5000
mn = float("inf")

for i in range(1,n):
	Pi = P(i)
	for j in range(i+1, n):
		Pj = P(j)
		d = abs(Pi-Pj)
		if isPentagonal(d) and isPentagonal(Pi+Pj):
			print (Pi, Pj)
			if d < mn:
				mn = d

print(mn)