# Checks if pandigital upto 9
def isPan (st):
	return sorted(list(st)) == list(s)


def isAns (i):
	ava = [1] * n
	for j in range(1,6):
		k = i*j
		for v in list(str(k)):
			if not ava[int(v) - 1]:
				return False
			else:
				ava[int(v) - 1] = 0

		if ava == [0] * n:
			return True

n = 9
s = "".join([str(x+1) for x in range(n)])


mn = 9
mx = 98765//2

for i in range(mn, mx, 2):
	if isAns (i):
		val = i

print(val, val*2, sep="")
