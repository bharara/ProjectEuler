n = 1001


s = [1]
for mul in range(2, n, 2):
	base  = s[len(s)-1]
	for i in range(1,5):
		s.append(i*mul + base)

print(sum(s))