# - Problem 25
# - 1000-digit Fibonacci Number
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

n = 1000

x = 0
y = 1

i = 0
while len(str(x)) < n:
    i += 1
    x, y = y, x+y
print (i)