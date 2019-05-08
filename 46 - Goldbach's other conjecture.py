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


for c in comp:
	k = c
	flag = False
	for pr in range(c-2, 1, -2):
		if isPrime(pr) and sqrt((c - pr)/2).is_integer():
			flag = True
			break

	if not flag:
		print(c)
		break
