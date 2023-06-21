# - Problem 46
# - Goldbach's Other Conjecture
# 
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import sqrt
n = 10000

comp = []
for i in range (9, n, 2):
	for j in range(3, int (sqrt(i) + 1), 2):
		if i%j == 0:
			comp.append (i)
			break


def isPrime (i):
	return i not in comp

def isGoldBack(n):
	for pr in range(c-2, 1, -2):
		if isPrime(pr) and sqrt((c - pr)/2).is_integer():
			return True
	return False
	
for c in comp:
	if not isGoldBack(c):
		print (c)
		break