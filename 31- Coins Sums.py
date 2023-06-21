# - Problem 31
# - Coin Sums
# 
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins?


n = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]


nb_ways = [1] + [0] * n
for c in coins:
	for v in range(n + 1 - c):
		nb_ways[v + c] += nb_ways[v]


print (nb_ways[-1])