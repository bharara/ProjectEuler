# - Problem 16
# - Power Digit Sum
# 
# What is the sum of the digits of the number 2^1000?

n = 1000
k = list(str(2**n))
s = sum(int(i) for i in k)

print(s)