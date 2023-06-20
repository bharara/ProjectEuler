n = 1001

s = 1
k = 1

for mul in range(2, n, 2):
	base  = k
	for i in range(1,5):
		k = i*mul + base
		s += k

print(s)