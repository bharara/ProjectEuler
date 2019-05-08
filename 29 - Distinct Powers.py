n = 100

ist= []
for a in range(2, n+1):
	for b in range(2, n+1):
		ist.append(a**b)
	
print(len(set(ist)))
