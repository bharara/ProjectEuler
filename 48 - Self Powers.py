# - Problem 48
# - Self Powers
# 
# Find the last ten digits of the series,  1^1 + 2^2 ... 1000^1000

n = 1000
total = sum(i**i for i in range (1, n+1))

print(str(total)[-10:])
