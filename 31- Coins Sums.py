def countWays(arr, m, N): 
	count = [0] * (N+1) 
	count[0] = 1; 

	for i in range(1, N+1):
		for j in range(m): 
			if (i >= arr[j]): 
				count[i] += count[i - arr[j]]

	return count[N]


N = 200
wt = [1, 2, 5, 10, 20, 50, 100, 200]
print(countWays(wt, 8, N))

# rows = len(wt) + 1
# col = W + 1

# table = []
# for i in range(rows):
# 	row = [0] * col
# 	table.append(row)

# for i in range(1, rows):
# 	for j in range(1, col):
# 		if j - i - 1 >= 0:
# 			table [i][j] = max(table[i-1][j], table[i-1][j - i - 1] + wt[i-1])
# 		elif i > j:
# 			table [i][j] = table[i-1][j]
# 		else:
# 			table [i][j] = max(table[i-1][j], wt[i-1])
# 		#print(table[i-1][j], table[i-1][j - wt[i-1]], wt[i-1])
# 	#printT(table)
 
# print(table)